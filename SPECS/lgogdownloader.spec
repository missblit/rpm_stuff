Name:           lgogdownloader
Version:        2.20
Release:        1%{?dist}
Summary:        LGOGDownloader is open source downloader to GOG.com for Linux users using the same API as the official GOGDownloader 
License:        WTFPL
URL:            https://sites.google.com/site/gogdownloader/home
Source0:        https://sites.google.com/site/gogdownloader/lgogdownloader-2.20.tar.gz
BuildRequires:  curl-devel, jsoncpp-devel, liboauth-devel, tinyxml-devel, htmlcxx, help2man
#Requires:       boost-filesystem, boost-iostreams, boost-program-options, boost-system, xz-libs, glibc

%description
LGOGDownloader is open source downloader to GOG.com for Linux users using the same API as the official GOGDownloader.

%prep
%autosetup

%build
make CFLAGS="-std=c++11 %{optflags}" BINDIR=%{_bindir}
#Seems to go wacky sometimes with _smp_mflags, but my laptop's too 
#slow to investigate without everything freezing up
#make %{?_smp_mflags} CFLAGS="-std=c++11 %{optflags}" BINDIR=%{_bindir}

%install
%make_install

%files
%doc
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}


%changelog
* Sun Dec 28 2014 Zoe Clifford <zoeacacia@gmail.com> - 2.20
- Initial version of the package
