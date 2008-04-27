
%define name	krusader
%define version	1.90.0
%define rel	1
%define release %mkrel %rel

%if %mdkversion <= 200710
%define __libtoolize /bin/true
%endif

Summary: 	Advanced KDE twin-panel file-manager
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://downloads.sourceforge.net/krusader/%{name}-%{version}.tar.gz
License: 	GPL
Group: 		File tools
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://krusader.sourceforge.net/
Epoch:		3
BuildRequires:  kdelibs-devel
BuildRequires:	kdebase-devel
BuildRequires:	kjsembed-devel
BuildRequires:	acl-devel
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

%prep
%setup -q

%build
export KDEDIR=%{_prefix}
%configure2_5x --disable-rpath

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#icons for rpmlint
mkdir -p %buildroot/{%_liconsdir,%_miconsdir,%{_iconsdir}}
ln -s %{_datadir}/icons/crystalsvg/48x48/apps/%{name}_user.png %buildroot/%_liconsdir
ln -s %{_datadir}/icons/crystalsvg/32x32/apps/%{name}_user.png %buildroot/%{_iconsdir}
ln -s %{_datadir}/icons/crystalsvg/16x16/apps/%{name}_user.png %buildroot/%_miconsdir
ln -s %{_datadir}/icons/crystalsvg/48x48/apps/%{name}_root.png %buildroot/%_liconsdir
ln -s %{_datadir}/icons/crystalsvg/32x32/apps/%{name}_root.png %buildroot/%{_iconsdir}
ln -s %{_datadir}/icons/crystalsvg/16x16/apps/%{name}_root.png %buildroot/%_miconsdir

%find_lang krusader

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%if %mdkversion > 200600
%{update_desktop_database}
%update_icon_cache crystalsvg
%endif

%postun
%{clean_menus}
%if %mdkversion > 200600
%clean_icon_cache crystalsvg
%clean_desktop_database
%endif

%files -f krusader.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO COPYING krusader.lsm
%doc %{_datadir}/doc/HTML/en/*
%{_bindir}/krusader
%{_datadir}/applications/kde/krusader*.desktop
%{_datadir}/apps/krusader
%{_datadir}/services/*
%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop
%{_datadir}/config/kio_isorc
%{_iconsdir}/crystalsvg/*/apps/krusader*.png
%{_iconsdir}/locolor/*/apps/krusader*.png
%{_miconsdir}/%{name}_*.png
%{_iconsdir}/%{name}_*.png
%{_liconsdir}/%{name}_*.png
%{_libdir}/kde3/*
%{_mandir}/man1/*

%lang(ru) %dir %_docdir/HTML/ru/krusader
%lang(ru) %doc %_docdir/HTML/ru/krusader/common
%lang(ru) %doc %_docdir/HTML/ru/krusader/*.bz2
%lang(ru) %doc %_docdir/HTML/ru/krusader/*.docbook
