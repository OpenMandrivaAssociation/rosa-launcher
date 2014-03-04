Name:		rosa-launcher
Version:	2.0.0
Release:	56
Epoch:		2
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/
Source0:	%{name}-%{version}.tar.gz
Source1:	om-simplewelcome.jpg
Source2:	mdk-simplewelcome.png
Patch0:		rosa-launcher-2.0.0-mdvbutton.patch
Patch1:		rosa-launcher-2.0.0-it.patch
Patch2:		rosa-launcher-2.0.0-background.png.patch
Requires:	kdebase4-workspace
Requires:	qjson
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	qjson-devel
BuildRequires:	pkgconfig(shared-desktop-ontologies)

%description
ROSA Desktop Application Launcher.

%prep
%setup -q
%patch0 -p1 -b .mdvbutton~
%patch1 -p1 -b .it~
%if "%{disttag}" == "mdk"
%patch2 -p1 -b .background~
%endif

%build
%cmake_kde4

%install
%makeinstall_std -C build

%if "%{disttag}" == "mdk"
install -m644 %{SOURCE2} -D %{buildroot}%{_datadir}/rosa-launcher/assets/background.png
%else
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
