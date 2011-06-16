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

%files
%defattr(-,root,root)
%_kde_bindir/rosa-launcher
%_kde_libdir/kde4/plasma_applet_rosa-launcher.so
%_kde_datadir/kde4/services/plasma-applet-rosa-launcher.desktop
/usr/share/locale/

%_kde_datadir/apps/plasma/plasmoids/rosastarter
%_kde_datadir/kde4/services/plasma-applet-rosastarter.desktop

%_kde_libdir/kde4/plasma_runner_rosa_services.so
%_kde_datadir/kde4/services/plasma-runner-rosa-services.desktop

#--------------------------------------------------------------------

%description
ROSA Desktop Application Launcher

%prep
%setup -q

%build
make build

%install
%__rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
