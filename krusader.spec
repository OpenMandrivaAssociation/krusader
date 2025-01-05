Summary:	Advanced KDE twin-panel file-manager
Name:		krusader
Version:	2.9.0
Release:	1
License:	GPLv2+
Group:		File tools
URL:		https://krusader.sourceforge.net/
Source0:	https://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Core5Compat)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6QmlCore)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	qt6-qtbase-theme-gtk3

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
%doc README AUTHORS ChangeLog TODO
%{_bindir}/krusader
%{_datadir}/applications/org.kde.krusader*.desktop
%{_datadir}/krusader
#{_datadir}/kservices5/*.protocol
%{_datadir}/kxmlgui5/krusader
%{_datadir}/metainfo/org.kde.krusader.appdata.xml
%{_sysconfdir}/xdg/kio_isorc
%{_iconsdir}/hicolor/*/apps/krusader*.png
%{_libdir}/qt6/plugins/kf6/kio/kio_iso.so
%{_libdir}/qt6/plugins/kf6/kio/kio_krarc.so
%{_mandir}/man1/krusader.1*

#--------------------------------------------------------------------

%prep
%autosetup -p1

%cmake   \
          -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
          -G Ninja
%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html --with-man
