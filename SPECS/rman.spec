Name:		rman
Version:	3.2 
Release:	7%{?dist}
Summary:	Converts man pages to various other formats

Group:		System Environment/Base
License:	Artistic
URL:		http://sourceforge.net/projects/polyglotman
Source0:	http://easynews.dl.sourceforge.net/sourceforge/polyglotman/rman-3.2.tar.gz
Patch0:		rman-3.2-safe_printf.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Parse formatted man pages and man page source from most flavors of UNIX.
Convert to HTML, ASCII, TkMan, DocBook, and other formats.


%prep
%setup -q
%patch0


%build
cp Makefile Makefile.orig
cat Makefile.orig \
|sed s?"^BINDIR =.*"?"BINDIR = %{_bindir}"? \
|sed s?"^MANDIR =.*"?"MANDIR = %{_mandir}/man1"? \
|sed s?"^CFLAGS =.*"?"CFLAGS = %{optflags} -finline-functions"? \
> Makefile

make %{?_smp_mflags}

pushd contrib
for file in `find . -type f`; do
sed -i 's?^#!/usr/local/bin/perl?#!%{_bindir}/perl?' ${file}
sed -i 's?\r??' ${file}
done
popd


%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_mandir}/man1
install -m755 rman %{buildroot}%{_bindir}/
install -m644 rman.1 %{buildroot}%{_mandir}/man1/


%clean
rm -rf %buildroot


%files
%defattr(-,root,root,-)
%doc CHANGES README-rman.txt rman.html contrib/
%{_bindir}/rman
%{_mandir}/man1/*



%changelog
* Sun Dec 28 2014 Zoe Clifford <zoeacacia@gmail.com> - 3.2-7
- Fix gcc compile error (unsafe format string)

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 3.2-6
- Rebuild (for F7).

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 3.2-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 José Matos <jamatos[AT]fc.up.pt> - 3.2-4
- Rebuild for FC-6.

* Fri Apr 28 2006 Michael A. Peters <mpeters@mac.com> - 3.2-3
- Minor cleanup to packaging

* Fri Apr 28 2006 Michael A. Peters <mpeters@mac.com> - 3.2-2
- Package the contrib directory with %%doc

* Thu Apr 27 2006 Michael A. Peters <mpeters@mac.com> - 3.2-1
- Initial packaging for Fedora Extras
