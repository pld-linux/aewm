Summary:	AEWM - the ascetic window manager
Summary(pl):	AEWM - "ascetyczny" zarz±dca okien
Name:		aewm
Version:	1.2.3
Release:	1
License:	MIT
Group:		X11/Window Managers
Source0:	http://www.red-bean.com/~decklin/aewm/%{name}-%{version}.tar.gz
# Source0-md5:	94fa24a6b83652bdb9d802be8cfcf048
Source1:	%{name}.desktop
URL:		http://www.red-bean.com/~decklin/aewm/
BuildRequires:	gtk+-devel
BuildRequires:	glibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
aewm is a minimal window manager for X11.

%description -l pl
aewm jet minimalnym zarz±dc± okien dla X11. Nie potrafi obs³ugiwaæ
ikon, wielu sesji, motywów, t³a itp. Nie jest zbyt konfigurowalny.

Jego zalet± jest prostota i szybko¶æ.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_wmpropsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT XROOT=%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
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
%{_mandir}/man1/*
%{_wmpropsdir}/*
