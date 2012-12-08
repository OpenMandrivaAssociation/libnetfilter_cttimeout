%define major 1
%define libname %mklibname netfilter_cttimeout %{major}
%define develname %mklibname netfilter_cttimeout -d

Summary:	Netfilter extended cttimeout infrastructure library
Name:		libnetfilter_cttimeout
Version:	1.0.0
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.netfilter.org/projects/%{name}/
Source0:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2.sig
BuildRequires:	pkgconfig(libmnl) >= 1.0.0

%description
libnetfilter_cttimeout is the userspace library that provides the programming
interface to the fine-grain connection tracking timeout infrastructure. With
this library, you can create, update and delete timeout policies that can be
attached to traffic flows. This library is used by conntrack-tools.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	netfilter_cttimeout-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon May 28 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2
+ Revision: 800927
- rebuild

* Mon May 28 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1
+ Revision: 800911
- initial Mandriva package
- Created package structure for libnetfilter_cttimeout.

