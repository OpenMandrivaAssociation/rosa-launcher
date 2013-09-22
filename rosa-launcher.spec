Name:		rosa-launcher
Version:	2.0.0
Release:	54.4
Epoch:		2
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/
Source0:	%{name}-%{version}.tar.gz
Source1:	om-simplewelcome.jpg
Patch0:		rosa-launcher-2.0.0-mdvbutton.patch
Patch1:		rosa-launcher-2.0.0-it.patch
Requires:	kdebase4-workspace qjson
BuildRequires:	kdebase4-workspace-devel qjson-devel
BuildRequires:	pkgconfig(shared-desktop-ontologies)

%description
ROSA Desktop Application Launcher

%prep
%setup -q
%patch0 -p1 -b .mdvbutton~
%patch1 -p1 -b .it

%build
%cmake_kde4

%install
%makeinstall_std -C build
cp %{SOURCE1} %{buildroot}%{_datadir}/rosa-launcher/assets/background.jpg

%find_lang ROSA_Launcher

%files -f ROSA_Launcher.lang
%{_bindir}/rosa-launcher
%{_libdir}/kde4/plasma_applet_rosastarter.so
%{_libdir}/libtimeframe.so
%{_datadir}/kde4/services/plasma-applet-rosastarter.desktop
%{_datadir}/rosa-launcher
%{_datadir}/timeframe
