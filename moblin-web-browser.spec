%define version 1.9.3
%define rel 1
%define use_git 0
%define gitcommit 56cc6cd9cbdc85eaa0224676fa55a5dc752532be

%if %{use_git}
%define release %mkrel 2.%{gitcommit}.%{rel}
%define sversion %{gitcommit}
%else
%define release %mkrel %{rel}
%define sversion %{version}
%endif

Name: moblin-web-browser
Summary: Moblin web browser
Group: Networking/WWW
Version: %{version}
License: LGPL
URL: http://www.moblin.org
Release: %{release}
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{sversion}.tar.bz2
Patch0: moblin-web-browser-1.9.3-idldir.patch
Patch1: moblin-web-browser-1.9.3-stagecheck.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: clutter-gtk-devel
BuildRequires: clutter-mozembed-devel
BuildRequires: mozilla-headless-services-devel
BuildRequires: xulrunner-headless-devel
BuildRequires: nbtk-devel
BuildRequires: libmesagl1-devel
BuildRequires: libunique-devel
BuildRequires: libgtk+2-devel
BuildRequires: startup-notification-devel
BuildRequires: libdbus-glib-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: moblin-panel-devel

Requires: xulrunner-headless
Requires: clutter-mozembed

%description
Moblin web browser

%prep
%setup -q -n %{name}-%{sversion}
%patch0 -p1
%patch1 -p1 -b .stagecheck

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x --enable-browser --enable-netpanel --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_libdir}/xulrunner-1.9.2a1pre*/*
%{_libexecdir}/moblin-panel-internet
%{_datadir}/dbus-1/services/*service
%{_datadir}/locale/*
