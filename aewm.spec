Summary:	aewm
Summary(pl):	aewm
Name:		aewm
Version:	0.9.5
Release:	1
Copyright:	Freely distributable
Group:		X11/Window Managers
Group(pl):	X11/Menad¿ero Onkien
Source:		http://members.home.com/decklin/%name/%name-%version.tar.gz
URL:		http://members.home.com/decklin/aewm/
Patch:		%name-DESTDIR.patch
BuildRequires:	gtk+-devel
BuildRequires:	XFree86-devel
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description

%description -l pl

%prep
%setup -q
%patch -p0 

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
(cd goodies;make RPM_OPT_FLAGS="$RPM_OPT_FLAGS")

gzip -9 README
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/bin
make DESTDIR=$RPM_BUILD_ROOT install

(cd goodies;install -s {xaw,gtk}-{panel,palette,switch} $RPM_BUILD_ROOT/%{_prefix}/bin)
(cd goodies; install -s gtk-palette2 $RPM_BUILD_ROOT%{_prefix}/bin)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/aewm
%attr(755,root,root) %{_bindir}/xaw-*
%attr(755,root,root) %{_bindir}/gtk-*
