Name:           slim
Version:        1.3.6
Release:        0
Summary:        SLiM Standalone X Login Manager
Group:          X Window System
License:        GPL
URL:            https://github.com/kramergroup/slim
Vendor:         KramerGroup
Source:         https://github.com/kramergroup/slim/releases/%{version}/%{name}-%{version}.tar.gz
Prefix:         %{_prefix}
Packager: 	    DenisKramer
BuildRoot:      %{_tmppath}/%{name}-root

%define _prefix /usr

%description
SLiM (Simple Login Manager) is a graphical login manager for X11.
It aims to be simple, fast and independent from the various
desktop environments.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p build
cd build
cmake .. -DUSE_PAM=no -DBUILD_SLIMLOCK=no
make

%install
cd build
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING TODO ChangeLog
%config(noreplace) /etc/%{name}.conf
%{_bindir}/slim
%{_libdir}/libslim.so
%{_libdir}/libslim.so.1.3.6
/lib/systemd/system/slim.service
%{_prefix}/share/man/*
%{_prefix}/share/slim/*
