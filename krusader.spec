%define beta beta3

Summary:	Advanced KDE twin-panel file-manager
Name:		krusader
Version:	2.4.0
Release:	0.%{beta}.1
Epoch:		3
License:	GPLv2+
Group:		File tools
URL:		http://krusader.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/krusader/%{name}-%{version}-%{beta}.tar.bz2
Patch0:		krusader-2.3.0-beta1-default-mimetypes.patch
BuildRequires:	kdebase4-devel
BuildRequires:	kdelibs4-devel

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
%{_kde_bindir}/krusader
%{_kde_applicationsdir}/krusader*.desktop
%{_kde_appsdir}/krusader
%{_kde_services}/*.protocol
%{_kde_configdir}/kio_isorc
%{_kde_iconsdir}/hicolor/*/apps/krusader*.png
%{_kde_iconsdir}/locolor/*/apps/krusader*.png
%{_kde_libdir}/kde4/*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%{beta}
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

