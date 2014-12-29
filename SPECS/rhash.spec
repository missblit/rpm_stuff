%define version 1.3.3
# major is the part of the shared library name after the .so
%define major 0
%define libname    librhash
%define devlibname librhash-devel

%define is_mandrake %(test -e /etc/mandrake-release && echo 1 || echo 0)
%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)
%define is_fedora %(test -e /etc/fedora-release && echo 1 || echo 0)

Summary:        Utility for computing hash sums and creating magnet links.
Name:           rhash
Version:        %{version}
Release:        1%{?dist}
License:        MIT
Group:          Applications/File
Vendor:         Novosibirsk, Animegorodok
Packager:       Aleksey Kravchenko
URL:            http://rhash.sourceforge.net/
Source:         http://downloads.sourceforge.net/rhash/rhash-%{version}-src.tar.gz
BuildRoot:      %{_builddir}/%{name}-%{version}-root
BuildRequires:  openssl-devel
%description
RHash is a console utility for calculation and verification of magnet links
and a wide range of hash sums like CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160,
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

Features:
 * Output in a predefined (SFV, BSD-like) or a user-defined format.
 * Calculation of Magnet links.
 * Ability to process directories recursively.
 * Updating hash files (adding hash sums of files missing in the hash file).
 * Portability: the program works the same on Linux, *BSD or Windows.

# LibRHash shared library, contains librhash.so.[major] only
%package -n %{libname}
Summary:        LibRHash shared library
Group:          System/Libraries
Provides:       librhash = %{version}-%{release}
Provides:       librhash.so.0()(64bit)
%description -n %{libname}
LibRHash is a professional, portable, thread-safe C library for computing
a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160,
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

%package -n %{devlibname}
Summary:        Headers and static library for LibRHash
Group:          Development/C
Requires:       %{libname} = %{version}
#(!) MANDATORY
Provides:       librhash-devel = %{version}-%{release}
%description -n %{devlibname}
LibRHash is a professional, portable, thread-safe C library for computing
a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1, SHA256, SHA512,
AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R 34.11-94, RIPEMD-160,
HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of data
for a long-term storing or transferring.

%prep
%setup

%build
%{__make} build-shared lib-static CFLAGS="$RPM_OPT_FLAGS -DNDEBUG -DUSE_OPENSSL -DOPENSSL_RUNTIME -rdynamic" LDFLAGS=-ldl

%check
%{__make} test-shared CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"

%install
%{__make} install-shared install-lib-static install-lib-shared PREFIX=/usr DESTDIR="$RPM_BUILD_ROOT" MANDIR="%{_mandir}" LIBDIR="%{_libdir}"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog dist/rhash.1.html
/usr/bin/*
/etc/rhashrc
%{_mandir}/man1/

%files -n %{devlibname}
%defattr(-,root,root)
%{_libdir}/librhash.a
%{_libdir}/librhash.so
%{_includedir}/*.h

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README ChangeLog
%{_libdir}/librhash.so.%{major}

%post   -n %{libname}
ldconfig

%postun -n %{libname}
ldconfig

%changelog
* Tue Aug  5 2014 Aleksey <rhash.admin@gmail.com> 1.3.3-1mdk
* Wed Jul  2 2014 Aleksey <rhash.admin@gmail.com> 1.3.2-1mdk
* Wed Jan 08 2014 Aleksey <rhash.admin@gmail.com> 1.3.1-1mdk
* Tue Jun 11 2013 Aleksey <rhash.admin@gmail.com> 1.3.0-1mdk
* Tue Dec 25 2012 Aleksey <rhash.admin@gmail.com> 1.2.10-1mdk
* Sat Apr 14 2012 Aleksey <rhash.admin@gmail.com> 1.2.9-1mdk
* Wed Sep 14 2011 Aleksey <rhash.admin@gmail.com> 1.2.8-1mdk
* Sun Aug 14 2011 Aleksey <rhash.admin@gmail.com> 1.2.7-1mdk
* Tue Jun 14 2011 Aleksey <rhash.admin@gmail.com> 1.2.6-1mdk
* Wed May 18 2011 Aleksey <rhash.admin@gmail.com> 1.2.5-1mdk
* Fri Apr 15 2011 Aleksey <rhash.admin@gmail.com> 1.2.4-1mdk
* Sun Mar 27 2011 Aleksey <rhash.admin@gmail.com> 1.2.3-1mdk
* Fri Jan 14 2011 Aleksey <rhash.admin@gmail.com> 1.2.2-1mdk
* Tue Dec 14 2010 Aleksey <rhash.admin@gmail.com> 1.2.1-1mdk
* Sun Nov 14 2010 Aleksey <rhash.admin@gmail.com> 1.2.0-1mdk
* Fri Oct 15 2010 Aleksey <rhash.admin@gmail.com> 1.1.9-1mdk
* Wed Apr 14 2010 Aleksey <rhash.admin@gmail.com> 1.1.8-1mdk
* Wed Mar 31 2010 Aleksey <rhash.admin@gmail.com> 1.1.7-1mdk
* Wed Feb 24 2010 Aleksey <rhash.admin@gmail.com> 1.1.6-1mdk
* Thu Jan 28 2010 Aleksey <rhash.admin@gmail.com> 1.1.5-1mdk
* Mon Dec 14 2009 Aleksey <rhash.admin@gmail.com> 1.1.4-1mdk
* Sun Nov 29 2009 Aleksey <rhash.admin@gmail.com> 1.1.3-1mdk
* Mon Jun 15 2009 Aleksey <rhash.admin@gmail.com> 1.1.2-1mdk
* Mon Mar 23 2009 Aleksey <rhash.admin@gmail.com> 1.1.1-1mdk
* Sat Mar 14 2009 Aleksey <rhash.admin@gmail.com> 1.1.0-1mdk
* Sat Feb 14 2009 Aleksey <rhash.admin@gmail.com> 1.0.8-1mdk
* Sun Dec 14 2008 Aleksey <rhash.admin@gmail.com> 1.0.7-1mdk
* Fri Nov 14 2008 Aleksey <rhash.admin@gmail.com> 1.0.6-1mdk
* Sun Sep 14 2008 Aleksey <rhash.admin@gmail.com> 1.0.5-1mdk
* Wed Jul  9 2008 Aleksey <rhash.admin@gmail.com> 1.0.4-1mdk
* Sat Jun 28 2008 Aleksey <rhash.admin@gmail.com> 1.0.3-1mdk
* Sat Jun 14 2008 Aleksey <rhash.admin@gmail.com> 1.0.2-1mdk
* Wed May 15 2008 Aleksey <rhash.admin@gmail.com> 1.0.1-1mdk
* Fri Dec 14 2007 Aleksey <rhash.admin@gmail.com> 1.0-1mdk
* Thu Sep 13 2007 Aleksey <rhash.admin@gmail.com> 0.9.2-1mdk
* Sun May 27 2007 Aleksey <rhash.admin@gmail.com> 0.9.1-1mdk
* Sun May 13 2007 Aleksey <rhash.admin@gmail.com> 0.9-1mdk
* Fri May 11 2007 Aleksey <rhash.admin@gmail.com> 0.8.9-1mdk
* Wed May 02 2007 Aleksey <rhash.admin@gmail.com> 0.8.8-1mdk
* Mon Apr 16 2007 Aleksey <rhash.admin@gmail.com> 0.8.7-1mdk
* Mon Mar 26 2007 Aleksey <rhash.admin@gmail.com> 0.8.6-1mdk
* Wed Jan 31 2007 Aleksey <rhash.admin@gmail.com> 0.8.5-1mdk
* Sun Nov 05 2006 Aleksey <rhash.admin@gmail.com> 0.8.4-1mdk
* Mon Apr 10 2006 Aleksey <rhash.admin@gmail.com> 0.8.3-1mdk
* Thu Mar 30 2006 Aleksey <rhash.admin@gmail.com> 0.8.2-1mdk
* Wed Jan 25 2006 Aleksey <rhash.admin@gmail.com> 0.8.1-1mdk
* Mon Jan 23 2006 Aleksey <rhash.admin@gmail.com> 0.8-1mdk
* Sat Jan 14 2006 Aleksey <rhash.admin@gmail.com> 0.7-1mdk
* Fri Sep 02 2005 Aleksey <rhash.admin@gmail.com> 0.6-1mdk
* Sun Aug 14 2005 Aleksey <rhash.admin@gmail.com> 0.5-1mdk
The first public version
