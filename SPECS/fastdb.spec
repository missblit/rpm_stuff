%define name fastdb
%define version 3.75

Summary: Main Memory Relational Database Management System
Name: %{name}
Version: %{version}
Release: 1%{?dist}
Source: %{name}-%{version}.tar.gz
License: Apache
URL: http://www.garret.ru/fastdb.html
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Object-Relational Main-Memory Embedded Database system tightly integrated
with C++ language. Use OS virtual mapping mechanism to access data.
Provides subset of SQL language with OO extensions. Support of
transactions, fault tolerance, replication.

%prep
%autosetup -n fastdb

%build
%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/fastdb/*

%changelog
* Thu Jul 30 2015 Zoe Clifford <zoeacacia@gmail.com>
+ Created spec at version 3.75
