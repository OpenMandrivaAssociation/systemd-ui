Summary:	System and Service Manager UI for systemd
Name:		systemd-ui
Version:	3
Release:	1
License:	GPLv2+
Group:		System/Configuration/Boot and Init
URL:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/systemd-ui-%{version}.tar.xz
Patch0:		systemd-ui-0-linkage_fix.diff
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	m4
BuildRequires:	libtool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	vala >= 0.11
BuildRequires:	xsltproc
Requires:	polkit
Requires:	systemd
Obsoletes:	systemd-gtk < 45
Provides:	systemd-gtk = %{version}-%{release}
Provides:	systemadm = %{version}-%{release}
Obsoletes:	systemadm <= 0-3

%description
Graphical front-end for systemd

It contains :
	* systemadm is a graphical frontend for the systemd system and service manager
          and allows introspection and control of systemd

%prep

%setup -q -n systemd-ui-%{version}
%patch0 p-1

%build
export CC=gcc
export CXX=g++

autoreconf -fi

%configure
%make

%install
%makeinstall_std

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/systemadm.desktop <<EOF
[Desktop Entry]
Name=Graphical front-end for systemd
Comment=Modify systemd configuration
Exec=systemadm
Terminal=false
Type=Application
Icon=development_tools_section
Categories=GTK;Settings;System;X-Mageia-CrossDesktop;
EOF

%files
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.*
%{_datadir}/applications/systemadm.desktop
