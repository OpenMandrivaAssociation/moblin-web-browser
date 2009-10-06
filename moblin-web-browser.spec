Name: moblin-web-browser
Summary: Moblin web browser
Group: Networking/WWW
Version: 1.9.3
License: LGPL
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: moblin-web-browser-1.9.3-idldir.patch
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

Requires: xulrunner-headless
Requires: clutter-mozembed

%description
Moblin web browser

%prep
%setup -q 
%patch0 -p1

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
