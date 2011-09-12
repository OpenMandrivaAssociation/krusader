Summary: 	Advanced KDE twin-panel file-manager
Name: 		krusader
Version: 	2.0.0
Release: 	%{mkrel 3}
Source0:	http://prdownloads.sourceforge.net/krusader/%name-%version.tar.gz
Patch0:		krusader-6249-fix-str-fmt.patch
# fixes krusader bug #2793916, window width gets bigger when path is long
Patch1:		krusader-svn987282-fix-window-width.patch
Patch2:		krusader-missing-include.patch
# submitted patch upstream in bug #229489
Patch3:		krusader-fix-crash-on-file-removal-race.patch
Patch4:		krusader-2.0.0-qt47.patch
Patch5:		krusader-2.0.0-gcc45.patch
Patch6:		%{name}.desktop.patch
License: 	GPLv2+
Group: 		File tools
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://krusader.sourceforge.net/
Epoch:		3
BuildRequires:  kdelibs4-devel
Obsoletes:	kde3-krusader < 2:1.02-4

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

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%clean_desktop_database
%endif

%files -f krusader.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO COPYING krusader.lsm
%{_kde_bindir}/krusader
%{_kde_datadir}/applications/kde4/krusader*.desktop
%{_kde_datadir}/apps/krusader
%{_kde_datadir}/kde4/services/*.protocol
%{_kde_datadir}/config/kio_isorc
%{_kde_iconsdir}/hicolor/*/apps/krusader*.png
%{_kde_iconsdir}/locolor/*/apps/krusader*.png
%{_kde_libdir}/kde4/*.so

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -Cbuild

%find_lang krusader --with-html

%clean
rm -rf $RPM_BUILD_ROOT
