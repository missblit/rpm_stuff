%define name htmlcxx
%define version 0.84

Summary: A html/css1 parser in C++
Name: %{name}
Version: %{version}
Release: 1%{?dist}
Source: %{name}-%{version}.tar.gz
License: LGPL
URL: http://htmlcxx.sf.net
BuildRoot: %{_tmppath}/%{name}-%{version}-root
#This patch simply adds a standard C++ header file to make g++ happy
Patch0:         htmlcxx-0.84-cstddef-header.patch
BuildRequires:  bison

%description
This is a html/css1 parser with politics created trying to mimic mozilla firefox
(http://www.mozilla.org) behavior. So you should expect parse trees similar to
those create by firefox. However, differently from firefox, htmlcxx does not
insert non-existent stuff in your html. Therefore, serializing the DOM tree
gives exactly the same bytes contained in the original HTML document.

%prep
%autosetup -p0

%build
%configure
#Get rid of pesky rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(755,root,root)
%{_bindir}/%{name}
%{_libdir}/*.so*
%{_libdir}/pkgconfig/%{name}.pc
%{_datarootdir}/htmlcxx/css/default.css
%exclude %{_libdir}/*.la

%package devel
Summary: Development headers for htmlcxx

%description devel
Development headers for htmlcxx.
%files devel
%{_includedir}/%{name}/*

%changelog
* Sun Dec 28 2014 Zoe Clifford <zoeacacia@gmail.com>
+ Update to 0.84. Adjust to play nice with Fedora
* Thu Jun 16 2006 Davi de Castro Reis <davi@akwan.com.br>
+ Version 0.80 released
* Thu Jun 9 2005 Davi de Castro Reis <davi@akwan.com.br>
+ Created spec
