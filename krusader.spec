Summary:	Advanced KDE twin-panel file-manager
Name:		krusader
Version:	2.6.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		File tools
URL:		http://krusader.sourceforge.net/
Source0:	http://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5GuiAddons)

%description
Krusader is an advanced twin panel (commander style) file manager
for KDE and other desktops in the *nix world, similar to Midnight or
Total Commander. It provides all the file management features you
could possibly want.

Plus: extensive archive handling, mounted filesystem support, FTP,
advanced search module, an internal viewer/editor, directory
synchronisation, file content comparisons, powerful batch renaming
and much much more. It supports a wide variety of archive formats
and can handle other KIO slaves such as smb or fish.

%files -f krusader.lang
%doc README AUTHORS ChangeLog TODO COPYING krusader.lsm
%{_bindir}/krusader
%{_datadir}/applications/org.kde.krusader*.desktop
%{_datadir}/krusader
%{_datadir}/kservices5/*.protocol
%{_datadir}/kxmlgui5/krusader
%{_datadir}/metainfo/org.kde.krusader.appdata.xml
%{_sysconfdir}/xdg/kio_isorc
%{_iconsdir}/hicolor/*/apps/krusader*.png
%{_libdir}/qt5/plugins/kio*.so
%{_mandir}/man1/krusader.1*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-html --with-man

