Name:		rosa-launcher
Version:	2.1.0
Release:	1
Epoch:		3
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/
Source0:	%{name}-%{version}.tar.bz2
Source1:	om-simplewelcome.jpg
Patch0:		rosa-launcher-2.0.0-mdvbutton.patch
Patch2:		rosa-launcher-2.0.0-background.png.patch
Requires:	kdebase4-workspace
Requires:	qjson
%if "%{disttag}" == "mdk"
Requires:	distro-theme-opaque-background
%endif
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	qjson-devel
BuildRequires:	pkgconfig(shared-desktop-ontologies)

%description
ROSA Desktop Application Launcher.

%prep
%setup -q
%patch0 -p1 -b .mdvbutton~
%if "%{disttag}" == "mdk"
%patch2 -p1 -b .background~
%endif

%build
%cmake_kde4

%install
%makeinstall_std -C build

%if "%{disttag}" != "mdk"
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/rosa-launcher/assets/background.jpg
%endif

%find_lang ROSA_Launcher

%files -f ROSA_Launcher.lang
%{_bindir}/rosa-launcher
%{_libdir}/kde4/plasma_applet_rosastarter.so
%{_libdir}/libtimeframe.so
%{_datadir}/kde4/services/plasma-applet-rosastarter.desktop
%{_datadir}/rosa-launcher
%{_datadir}/timeframe
