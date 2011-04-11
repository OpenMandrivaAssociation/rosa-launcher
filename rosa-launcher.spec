Name:		rosa-launcher
Summary:	ROSA Desktop Application Launcher
Version:	0.15.2
Release:	%mkrel 2
Source0:	rosa-launcher-%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	GPLv3
BuildArch: noarch

Requires: kdebase4-workspace
BuildRequires: kde4-macros
Requires:       python-kde4
Requires:       plasma-scriptengine-python
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  kdebase4-devel

%description
ROSA Desktop Application Launcher

%prep
%setup -q

%build
make build

%install
%__rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

%clean 
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_kde_bindir/rosa-launcher
%_kde_libdir/kde4/plasma_applet_rosa-launcher.so
%_kde_datadir/kde4/services/plasma-applet-rosa-launcher.desktop
/usr/share/locale/

%_kde_datadir/apps/plasma/plasmoids/rosastarter
%_kde_datadir/kde4/services/plasma-applet-rosastarter.desktop

