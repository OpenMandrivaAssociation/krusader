%define name krusader
%define version 1.80.0
%define rel 0.beta2.1
%define release %mkrel %rel

Summary: 	Advanced twin-panel file-manager for KDE 3.x
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%name-%{version}-beta2.tar.bz2
License: 	GPL
Group: 		File tools
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://krusader.sourceforge.net
Epoch:		3
Requires: 	kdelibs

BuildRequires:  kdelibs-devel

Obsoletes:	kde3-krusader
Provides:	kde3-krusader

%description
Krusader is an advanced twin-panel (commander-style) file-manager for KDE 3.x
(similar to Midnight or Total Commander) but with many extras.
It provides all the file-management features you could possibly want.
Plus: extensive archive handling, mounted filesystem support, FTP,
advanced search module,
viewer/editor, directory synchronisation, file content comparisons,
powerful batch renaming and
much much more.
It supports the following archive formats: tar, zip, bzip2, gzip, rar,
ace, arj and rpm
and can handle other KIOSlaves such as smb:// or fish://
It is (almost) completely customizable, very user friendly,
fast and looks great on your desktop! :-)
You should give it a try. 

%prep
%setup -q -n %name-%{version}-beta2

%build
make -f admin/Makefile.common cvs

%{?__cputoolize: %{__cputoolize} }

# %%configure doesn't work
./configure --prefix=%_prefix \
	--bindir=%_bindir \
	--libdir=%_libdir \
%if "%{_lib}" != "lib"
    --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
	--datadir=%{_datadir} \
        --disable-rpath \
	--disable-debug 

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall KDEDIR=$RPM_BUILD_ROOT%{_prefix} kde_minidir=$RPM_BUILD_ROOT%{_miconsdir}

#fix conflict with Kdebase
rm -fr %buildroot%{_libdir}/kde3/kio_tar.so
rm -fr %buildroot%{_libdir}/kde3/kio_tar.la

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}

kdedesktop2mdkmenu.pl krusader "System/File Tools" %buildroot/%{_datadir}/applications/kde/krusader.desktop %buildroot/%_menudir/krusader
kdedesktop2mdkmenu.pl krusader "System/File Tools" %buildroot/%{_datadir}/applications/kde/krusader_root-mode.desktop temp.menu
#echo >> %buildroot/%_menudir/krusader
#cat temp.menu >> %buildroot/%_menudir/krusader

#icons for rpmlint
mkdir -p %buildroot/{%_liconsdir,%_miconsdir,%{_iconsdir}}
ln -s %{_datadir}/icons/crystalsvg/48x48/apps/%{name}_user.png %buildroot/%_liconsdir
ln -s %{_datadir}/icons/crystalsvg/32x32/apps/%{name}_user.png %buildroot/%{_iconsdir}
ln -s %{_datadir}/icons/crystalsvg/16x16/apps/%{name}_user.png %buildroot/%_miconsdir
ln -s %{_datadir}/icons/crystalsvg/48x48/apps/%{name}_root.png %buildroot/%_liconsdir
ln -s %{_datadir}/icons/crystalsvg/32x32/apps/%{name}_root.png %buildroot/%{_iconsdir}
ln -s %{_datadir}/icons/crystalsvg/16x16/apps/%{name}_root.png %buildroot/%_miconsdir
rm -rf $RPM_BUILD_ROOT/%{_datadir}/mimelnk/application/*.desktop


%find_lang krusader

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%if %mdkversion > 200600
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache locolor
%endif

%postun
%{clean_menus}
%if %mdkversion > 200600
%clean_icon_cache crystalsvg
%clean_icon_cache locolor
%clean_desktop_database
%endif

%files -f krusader.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO COPYING krusader.lsm
%doc %{_datadir}/doc/HTML/en/*
%{_bindir}/*
%{_datadir}/applications/kde/krusader*.desktop

%{_datadir}/apps/krusader/*.color
%{_datadir}/apps/krusader/*.keymap*
%{_datadir}/apps/krusader/*.xml

%dir %{_datadir}/apps/krusader/
%{_datadir}/apps/krusader/*.rc
%{_datadir}/apps/krusader/*.png

%{_datadir}/services/*

%_menudir/*

%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop
%{_datadir}/config/kio_isorc

%{_datadir}/apps/krusader/icons/crystalsvg/16x16/actions/*.png
%{_datadir}/apps/krusader/icons/crystalsvg/22x22/actions/*.png
%{_datadir}/apps/krusader/icons/crystalsvg/32x32/actions/*.png

%{_iconsdir}/crystalsvg/16x16/apps/krusader_blue.png
%{_iconsdir}/crystalsvg/16x16/apps/krusader_red.png
%{_iconsdir}/crystalsvg/22x22/apps/krusader_blue.png
%{_iconsdir}/crystalsvg/22x22/apps/krusader_red.png
%{_iconsdir}/crystalsvg/22x22/apps/krusader_shield.png
%{_iconsdir}/crystalsvg/32x32/apps/krusader_blue.png
%{_iconsdir}/crystalsvg/32x32/apps/krusader_red.png
%{_iconsdir}/crystalsvg/32x32/apps/krusader_shield.png
%{_iconsdir}/crystalsvg/48x48/apps/krusader_blue.png
%{_iconsdir}/crystalsvg/48x48/apps/krusader_red.png
%{_iconsdir}/crystalsvg/48x48/apps/krusader_shield.png
%{_iconsdir}/crystalsvg/64x64/apps/krusader_blue.png
%{_iconsdir}/crystalsvg/64x64/apps/krusader_red.png
%{_iconsdir}/crystalsvg/64x64/apps/krusader_shield.png

%{_iconsdir}/crystalsvg/16x16/apps/krusader_root.png
%{_iconsdir}/crystalsvg/16x16/apps/krusader_user.png
%{_iconsdir}/crystalsvg/22x22/apps/krusader_root.png
%{_iconsdir}/crystalsvg/22x22/apps/krusader_user.png
%{_iconsdir}/crystalsvg/32x32/apps/krusader_root.png
%{_iconsdir}/crystalsvg/32x32/apps/krusader_user.png
%{_iconsdir}/crystalsvg/48x48/apps/krusader_root.png
%{_iconsdir}/crystalsvg/48x48/apps/krusader_user.png
%{_iconsdir}/crystalsvg/64x64/apps/krusader_root.png
%{_iconsdir}/crystalsvg/64x64/apps/krusader_user.png


%{_iconsdir}/locolor/16x16/apps/krusader.png
%{_iconsdir}/locolor/32x32/apps/krusader.png
%{_iconsdir}/locolor/32x32/apps/krusader2.png

%{_datadir}/apps/krusader/icons/crystalsvg/16x16/apps/krusader_root.xpm
%{_datadir}/apps/krusader/icons/crystalsvg/16x16/apps/krusader_user.xpm
%{_datadir}/apps/krusader/icons/crystalsvg/32x32/apps/krusader_root.xpm
%{_datadir}/apps/krusader/icons/crystalsvg/32x32/apps/krusader_user.xpm

%{_miconsdir}/%{name}_*.png
%{_iconsdir}/%{name}_*.png
%_liconsdir/%{name}_*.png

%{_libdir}/kde3/*

%{_mandir}/man1/*
%dir %_docdir/HTML/ru/krusader/
%doc %_docdir/HTML/ru/krusader/common
%doc %_docdir/HTML/ru/krusader/*.bz2
%doc %_docdir/HTML/ru/krusader/*.docbook


