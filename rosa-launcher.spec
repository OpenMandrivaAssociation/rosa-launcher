Name:		rosa-launcher
Version:	0.25
Release:	1
Summary:	ROSA Desktop Application Launcher
Group:		Graphical desktop/KDE
License:	GPLv3
URL:		http://www.rosalab.ru/
Source0:	rosa-launcher-%{version}.tar.gz

Requires:       kdebase4-workspace
Requires:       python-kde4
Requires:       plasma-scriptengine-python
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  kdebase4-devel

%description
ROSA Desktop Application Launcher

%files
%defattr(-,root,root)
%_kde_bindir/rosa-launcher
%_kde_libdir/kde4/plasma_applet_rosa-launcher.so
%_kde_datadir/kde4/services/plasma-applet-rosa-launcher.desktop
%_localedir/*

%_kde_datadir/apps/plasma/plasmoids/rosastarter
%_kde_datadir/kde4/services/plasma-applet-rosastarter.desktop

%_kde_libdir/kde4/plasma_runner_rosa_services.so
%_kde_datadir/kde4/services/plasma-runner-rosa-services.desktop

#--------------------------------------------------------------------

%prep
%setup -q

%build
%make build

%install
%makeinstall_std

%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
