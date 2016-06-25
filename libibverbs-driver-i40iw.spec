Summary:	Userspace driver for the Intel Ethernet Connection X722 RDMA adapters
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart RDMA Intel Ethernet Connection X722
Name:		libibverbs-driver-i40iw
Version:	0.5.223
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/libi40iw/libi40iw-%{version}.tar.gz
# Source0-md5:	ba54402259cc96f0e53b0659a9c58280
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
# only checked for, not used
#BuildRequires:	sysfsutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
libi40iw is a userspace driver for the Intel Ethernet Connection X722
RDMA adapters. It works as a plug-in module for libibverbs that allows
programs to use RDMA hardware directly from userspace.

%description -l pl.UTF-8
libi40iw to sterownik przestrzeni użytkownika dla kart RDMA Intel
Ethernet Connection X722 RDMA. Działa jako moduł ładowany przez
libibverbs, pozwalający programom na dostęp z przestrzeni użytkownika
do sprzętu RDMA.

%package static
Summary:	Static version of i40iw driver
Summary(pl.UTF-8):	Statyczna wersja sterownika i40iw
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of i40iw driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika i40iw, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libi40iw-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libi40iw.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libi40iw-rdmav2.so
%{_sysconfdir}/libibverbs.d/i40iw.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libi40iw.a
