Summary:	AEWM - the ascetic window manager
Summary(pl):	AEWM - "ascetyczny" menad¿er okien
Name:		aewm
Version:	1.1.2
Release:	2
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	http://www.red-bean.com/~decklin/aewm/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.red-bean.com/%7Edecklin/aewm/
BuildRequires:	gtk+-devel
BuildRequires:	glibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
aewm is a minimal window manager for X11.

%description -l pl
aewm jet minimalnym menad¿erem okien dla X11. Nie potrafi obs³ugiwaæ
ikon, wielu sesji, tematów, t³a itp. Nie jest zbyt konfigurowalny.

Jego zalet± jest prostota i szybko¶æ.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"
%{__make} -C goodies CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_wmpropsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

(cd goodies; install {xaw,gtk}-{panel,palette,switch} $RPM_BUILD_ROOT/%{_bindir})

install %{SOURCE1} $RPM_BUILD_ROOT/%{_wmpropsdir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_wmpropsdir}/*
