Summary:	AEWM - the ascetic window manager
Summary(pl):	AEWM - "ascetyczny" zarz�dca okien
Name:		aewm
Version:	1.2.3
Release:	2
License:	MIT
Group:		X11/Window Managers
Source0:	http://www.red-bean.com/~decklin/aewm/%{name}-%{version}.tar.gz
# Source0-md5:	94fa24a6b83652bdb9d802be8cfcf048
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Patch0:		%{name}-xft.patch
Patch1:		%{name}-amd64.patch
URL:		http://www.red-bean.com/~decklin/aewm/
BuildRequires:	gtk+-devel
BuildRequires:	lesstif-devel
BuildRequires:	xft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
aewm is a minimal window manager for X11.

%description -l pl
aewm jet minimalnym zarz�dc� okien dla X11. Nie potrafi obs�ugiwa�
ikon, wielu sesji, motyw�w, t�a itp. Nie jest zbyt konfigurowalny.

Jego zalet� jest prostota i szybko��.

%prep
%setup -q
%patch0 -p1
%ifarch amd64
%patch1 -p1
%endif

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_wmpropsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	XROOT=%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{aemenu-*,aepanel-*,aesession.*,set-gnome-pda.*}
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
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/*
%{_mandir}/man1/*
