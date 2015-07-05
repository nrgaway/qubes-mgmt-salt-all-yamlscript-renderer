%{!?version: %define version %(cat version)}
%{!?rel: %define rel %(cat rel)}
%{!?formula_name: %define formula_name %(cat formula_name)}

Name:      qubes-mgmt-salt-base-yamlscript-renderer
Version:   %{version}
Release:   %{rel}%{?dist}
Summary:   Combines python and YAML in a nice human readable format
License:   GPL 2.0
URL:	   http://www.qubes-os.org/

Group:     System administration tools
BuildArch: noarch
Requires:  qubes-mgmt-salt-config

%define _builddir %(pwd)

%description
Combines python and YAML in a nice human readable format.
All the power of python with readability of YAML.

%prep
# we operate on the current directory, so no need to unpack anything
# symlink is to generate useful debuginfo packages
rm -f %{name}-%{version}
ln -sf . %{name}-%{version}
%setup -T -D

%build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}

%files
%defattr(-,root,root)
%attr(750, root, root) %dir /srv/formulas/base/%{formula_name}
/srv/formulas/base/%{formula_name}/*

%changelog
