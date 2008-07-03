
%define name	krusader
%define version	2.0
%define snapshot 6014
%define rel	1

%if %snapshot
%define release	%mkrel 0.svn%snapshot.%rel
%else
%define release %mkrel %rel
%endif

Summary: 	Advanced KDE twin-panel file-manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
%if %snapshot
# http://krusader.svn.sourceforge.net/svnroot/krusader/trunk/krusader_kde4
Source:		%{name}-%{snapshot}.tar.bz2
%else
Source: 	http://downloads.sourceforge.net/krusader/%{name}-%{version}.tar.gz
%endif
License: 	GPL
Group: 		File tools
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://krusader.sourceforge.net/
Epoch:		3
BuildRequires:  kdelibs4-devel
Obsoletes:	kde3-krusader < 2:1.02-4
Provides:	kde3-krusader
# crystalsvg:
Requires(post):	kdelibs-common
Requires(postun): kdelibs-common

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
%doc %{_kde_datadir}/doc/HTML/en/*
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
%if %snapshot
%setup -q -n %name-%snapshot
%else
%setup -q
%endif

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -Cbuild

%find_lang krusader

%clean
rm -rf $RPM_BUILD_ROOT
