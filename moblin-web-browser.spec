%define version 2.1.1
%define rel 4
%define use_git 0
%define gitcommit 0
#56cc6cd9cbdc85eaa0224676fa55a5dc752532be

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
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: moblin-web-browser-1.9.3-idldir.patch
Patch1: moblin-web-browser-1.9.3-lib64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: clutter-gtk-devel
BuildRequires: clutter-mozembed-devel
BuildRequires: mozilla-headless-services-devel
BuildRequires: xulrunner-headless-devel
BuildRequires: nbtk-devel
BuildRequires: mesagl-devel
BuildRequires: unique-devel
BuildRequires: libgtk+2-devel
BuildRequires: startup-notification-devel
BuildRequires: libdbus-glib-devel
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: moblin-panel-devel
BuildRequires: zip

Requires: xulrunner-headless
Requires: clutter-mozembed

%description
Moblin web browser

%package panel
Summary: Moblin web panel
Group: Networking/WWW
Requires: %{name} = %{version}-%{release}

%description panel
Moblin web panel

%prep
%setup -q -n %{name}-%{sversion}
%patch0 -p1
%patch1 -p1 -b .lib64

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x --enable-browser --enable-netpanel --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_libdir}/xulrunner-1.9.2a1pre*/*

%files panel
%defattr(-,root,root,-)
%{_libexecdir}/moblin-panel-internet
%{_datadir}/dbus-1/services/*service
