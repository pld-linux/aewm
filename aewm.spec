Summary:	AEWM - the ascetic window manager
Summary(pl):	AEWM - "ascetyczny" menad¿er okien
Name:		aewm
Version:	0.9.6
Release:	1
Copyright:	Freely distributable
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy Okien
Source:		http://members.home.com/decklin/%name/%{name}-%{version}.tar.gz
Source1:	aewm.desktop
Patch0:		aewm-Makefile.patch
URL:		http://members.home.com/decklin/aewm/
BuildRequires:	gtk+-devel
BuildRequires:	glibc-devel
BuildRequires:	glib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6
%define	_mandir	/usr/X11R6/man

%description
aewm is a minimal window manager for X11. 

%description -l pl
aewm jet minimalnym menad¿erem okien dla X11. Nie potrafi obs³ugiwaæ ikon,
wielu sesji, tematów, t³a itp. Nie jest zbyt configurowa³ny.

Jego zalet± jest prostota i szybko¶æ.

%prep
%setup -q

%patch0

%build
make
make -C goodies

gzip -9 README
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/bin
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

make install XROOT=$RPM_BUILD_ROOT%{_prefix}

(cd goodies;install -s {xaw,gtk}-{panel,palette,switch} $RPM_BUILD_ROOT/%{_prefix}/bin)
(cd goodies; install -s gtk-palette2 $RPM_BUILD_ROOT%{_prefix}/bin)

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/aewm
%attr(755,root,root) %{_bindir}/xaw-*
%attr(755,root,root) %{_bindir}/gtk-*
%{_datadir}/gnome/wm-properties/aewm.desktop
