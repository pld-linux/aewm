Summary:	AEWM - the ascetic window manager
Summary(pl.UTF-8):	AEWM - "ascetyczny" zarządca okien
Name:		aewm
Version:	1.3.1
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	http://www.red-bean.com/~decklin/aewm/%{name}-%{version}.tar.gz
# Source0-md5:	d357a30c29540101d0545a3c9167bba0
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Patch0:		%{name}-xft.patch
Patch1:		%{name}-amd64.patch
URL:		http://www.red-bean.com/~decklin/aewm/
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	motif-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
aewm is a minimal window manager for X11. It doesn't support icons,
multiple sessions, themes or so; it isn't even highly customizable.
Its main benefits are simplicity and speed.

%description -l pl.UTF-8
aewm jet minimalnym zarządcą okien dla X11. Nie potrafi obsługiwać
ikon, wielu sesji, motywów, tła itp. Nie jest zbyt konfigurowalny.
Jego zaletą jest prostota i szybkość.

%prep
%setup -q
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	XROOT=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/X11/%{name}} \
	$RPM_BUILD_ROOT%{_wmpropsdir} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	XROOT=%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install src/aewmrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/aewmrc
install clients/clientsrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}/clientsrc

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{aemenu-*,aepanel-*,aesession.*,set-gnome-pda.*,switch-desk.*}
echo ".so aeclients.1x" > $RPM_BUILD_ROOT%{_mandir}/man1/aemenu-gtk.1x
echo ".so aeclients.1x" > $RPM_BUILD_ROOT%{_mandir}/man1/aemenu-xaw.1x
echo ".so aeclients.1x" > $RPM_BUILD_ROOT%{_mandir}/man1/aepanel-gtk.1x
echo ".so aeclients.1x" > $RPM_BUILD_ROOT%{_mandir}/man1/aepanel-xaw.1x
echo ".so aeclients.1x" > $RPM_BUILD_ROOT%{_mandir}/man1/aesession.1x
echo ".so aeclients.1x" > $RPM_BUILD_ROOT%{_mandir}/man1/set-gnome-pda.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/%{name}/*rc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/*
%{_mandir}/man1/*
