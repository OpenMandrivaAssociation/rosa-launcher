Name:		rosa-launcher
Summary:	ROSA Desktop Application Launcher
Version:	0.18.2
Release:	1
Source0:	rosa-launcher-%{version}.tar.gz
Group:		Graphical desktop/KDE
License:	GPLv3


Requires:       kdebase4-workspace
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

%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean 
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_kde_bindir/rosa-launcher
%_kde_libdir/kde4/plasma_applet_rosa-launcher.so
%_kde_datadir/kde4/services/plasma-applet-rosa-launcher.desktop
%_localedir

%_kde_datadir/apps/plasma/plasmoids/rosastarter
%_kde_datadir/kde4/services/plasma-applet-rosastarter.desktop

%changelog
* Fri Apr 08 2011 Aleksey Yermakov 0.15
- First cooker candidate

* Wed Dec 22 2010 Aleksey Yermakov 0.1
- Initial release
