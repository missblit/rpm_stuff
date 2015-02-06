%global commit 5fa53602da4d83badc457850fbf7aa501f170bde
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           Arena-Tracker
Version:        %{shortcommit}
Release:        1%{?dist}
Summary:        An arena card tracker for hearthstone.
License:        GPLv2
URL:            https://github.com/supertriodo/Arena-Tracker
Source0:        https://github.com/supertriodo/Arena-Tracker/archive/%{commit}/Arena-Tracker-%{commit}.tar.gz
BuildRequires:  qt5-qtbase-devel qt5-qtbase-gui

%description
Arena Tracker reads the Hearthstone log to keep track of your arena games and
rewards. It connects to www.arenamastery.com and automatically upload them to
your account. Watch the remaining cards of your arena deck while you play.

%prep
%setup -qn %{name}-%{commit}

%build
qmake-qt5 ArenaTracker.pro
make %{?_smp_mflags} CFLAGS="-std=c++11 %{optflags}" BINDIR=%{_bindir}

%install
mkdir -p %{buildroot}/%{_bindir}
install ArenaTracker %{buildroot}/%{_bindir}

%files
%{_bindir}/ArenaTracker


%changelog
* Fri Feb 6 2015 Zoe Clifford <zoeacacia@gmail.com> - 5fa53602da
- Initial version of the spec
