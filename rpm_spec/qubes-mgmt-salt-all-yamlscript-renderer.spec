%{!?version: %define version %(make get-version)}
%{!?rel: %define rel %(make get-release)}
%{!?package_name: %define package_name %(make get-package_name)}
%{!?package_summary: %define package_summary %(make get-summary)}
%{!?package_description: %define package_description %(make get-description)}

%{!?formula_name: %define formula_name %(make get-formula_name)}
%{!?state_name: %define state_name %(make get-state_name)}
%{!?saltenv: %define saltenv %(make get-saltenv)}
%{!?pillar_dir: %define pillar_dir %(make get-pillar_dir)}
%{!?formula_dir: %define formula_dir %(make get-formula_dir)}

Name:      %{package_name}
Version:   %{version}
Release:   %{rel}%{?dist}
Summary:   %{package_summary}
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt

%define _builddir %(pwd)

%description
%{package_description}

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%post
# Update Salt Configuration
qubesctl state.sls config -l quiet --out quiet > /dev/null || true
qubesctl saltutil.clear_cache -l quiet --out quiet > /dev/null || true
qubesctl saltutil.sync_all refresh=true -l quiet --out quiet > /dev/null || true

# Enable Test States
#qubesctl top.enable %{state_name} saltenv=test -l quiet --out quiet > /dev/null || true
#qubesctl top.enable %{state_name}.default saltenv=test -l quiet --out quiet > /dev/null || true

# Enable Test Pillar States
#qubesctl top.enable %{state_name} saltenv=test pillar=true -l quiet --out quiet > /dev/null || true

%files
%defattr(-,root,root)
%doc LICENSE README.rst README.tests
%attr(750, root, root) %dir /srv/salt/_renderers
/srv/salt/_renderers/pyobjects.py*
/srv/salt/_renderers/yamlscript.py*

%attr(750, root, root) %dir /srv/salt/_utils
/srv/salt/_utils/voluptuous.py*
/srv/salt/_utils/yamlscript_utils.py*

%attr(750, root, root) %dir /srv/formulas/test/yamlscript-formula
/srv/formulas/test/yamlscript-formula/LICENSE
/srv/formulas/test/yamlscript-formula/README.rst
/srv/formulas/test/yamlscript-formula/README.tests
/srv/formulas/test/yamlscript-formula/yamlscript/default.sls
/srv/formulas/test/yamlscript-formula/yamlscript/dev/gitfs.conf
/srv/formulas/test/yamlscript-formula/yamlscript/dev/pylintrc
/srv/formulas/test/yamlscript-formula/yamlscript/dev/.pylintrc
/srv/formulas/test/yamlscript-formula/yamlscript/dev/salt-call.py*
/srv/formulas/test/yamlscript-formula/yamlscript/dev/tox.ini
/srv/formulas/test/yamlscript-formula/yamlscript/init.sls
/srv/formulas/test/yamlscript-formula/yamlscript/init.top
/srv/formulas/test/yamlscript-formula/yamlscript/pillar/yamlscript/groups.sls
/srv/formulas/test/yamlscript-formula/yamlscript/pillar/yamlscript/users.sls
/srv/formulas/test/yamlscript-formula/yamlscript/pillar/yamlscript/users.top
/srv/formulas/test/yamlscript-formula/yamlscript/sudo.sls
/srv/formulas/test/yamlscript-formula/yamlscript/tests.bobby
/srv/formulas/test/yamlscript-formula/yamlscript/tests.docker
/srv/formulas/test/yamlscript-formula/yamlscript/tests.ems_service
/srv/formulas/test/yamlscript-formula/yamlscript/tests.mel
/srv/formulas/test/yamlscript-formula/yamlscript/tests.sudo
/srv/formulas/test/yamlscript-formula/yamlscript/tests.tester
/srv/formulas/test/yamlscript-formula/yamlscript/tests.vim
/srv/formulas/test/yamlscript-formula/yamlscript/vim/absent.sls
/srv/formulas/test/yamlscript-formula/yamlscript/vim/init.sls
/srv/formulas/test/yamlscript-formula/yamlscript/vim/salt-vim/ftdetect/sls.vim
/srv/formulas/test/yamlscript-formula/yamlscript/vim/salt-vim/ftplugin/sls.vim
/srv/formulas/test/yamlscript-formula/yamlscript/vim/salt-vim/LICENSE
/srv/formulas/test/yamlscript-formula/yamlscript/vim/salt-vim/README.rst
/srv/formulas/test/yamlscript-formula/yamlscript/vim/salt-vim/syntax/sls.vim
/srv/formulas/test/yamlscript-formula/yamlscript/vim/vimrc

%attr(750, root, root) %dir /srv/pillar/test/yamlscript
%config(noreplace) /srv/pillar/test/yamlscript/users.sls
%config(noreplace) /srv/pillar/test/yamlscript/groups.sls
/srv/pillar/test/yamlscript/users.top

%changelog
