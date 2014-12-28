Name:           innoextract
Version:        1.4
Release:        1%{?dist}
Summary:        A tool to unpack installers created by Inno Setup
License:        zlib
URL:            http://constexpr.org/innoextract/
Source0:        http://constexpr.org/innoextract/files/innoextract-1.4.tar.gz
BuildRequires:  boost-devel, xz-devel, glibc-devel
#Requires:       boost, xz-libs, glibc

%description
Inno Setup is a tool to create installers for Microsoft Windows applications.
innoextract allows to extract such installers under non-Windows systems without running the actual installer using wine.
innoextract currently supports installers created by Inno Setup 1.2.10 to 5.5.5.

%prep
%autosetup

%build
%cmake
make %{?_smp_mflags}

%install
%make_install

%files
%doc CHANGELOG LICENSE VERSION README.md
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}

%changelog
* Sun Dec 28 2014 Zoe Clifford <zoeacacia@gmail.com> - 1.4
- Initial version of the package
