Summary:	AEWM - the ascetic window manager
Summary(pl):	AEWM - "ascetyczny" menad¿er okien
Name:		aewm
Version:	0.9.6
Release:	1
Copyright:	Freely distributable
Group:		X11/Window Managers
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	http://members.home.com/decklin/%name/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://members.home.com/decklin/aewm/
BuildRequires:	gtk+-devel
BuildRequires:	glibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6
%define	_mandir	/usr/X11R6/man

%description
aewm is a minimal window manager for X11.

%description -l pl
aewm jet minimalnym menad¿erem okien dla X11. Nie potrafi obs³ugiwaæ
ikon, wielu sesji, tematów, t³a itp. Nie jest zbyt configurowa³ny.

Jego zalet± jest prostota i szybko¶æ.

%prep
%setup -q

%patch0

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"
%{__make} -C goodies CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

%{__make} install XROOT=$RPM_BUILD_ROOT%{_prefix}

(cd goodies;install -s {xaw,gtk}-{panel,palette,switch} $RPM_BUILD_ROOT/%{_bindir})
(cd goodies; install -s gtk-palette2 $RPM_BUILD_ROOT%{_bindir})

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/aewm
%attr(755,root,root) %{_bindir}/xaw-*
%attr(755,root,root) %{_bindir}/gtk-*
%{_datadir}/gnome/wm-properties/aewm.desktop
