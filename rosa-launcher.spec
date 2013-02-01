Name:		rosa-launcher
Version:	2.0.0
Release:	48
Epoch:		1
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/
Source0:	%{name}-%{version}.tar.gz

Requires:	kdebase4-workspace qjson
BuildRequires:	kdebase4-workspace-devel qjson-devel

%description
ROSA Desktop Application Launcher

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

%find_lang ROSA_Launcher

%files -f ROSA_Launcher.lang
%{_bindir}/rosa-launcher
%{_libdir}/kde4/plasma_applet_rosastarter.so
%{_libdir}/libtimeframe.so
%{_datadir}/kde4/services/plasma-applet-rosastarter.desktop
%{_datadir}/rosa-launcher
%{_datadir}/timeframe
