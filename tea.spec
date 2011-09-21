Name:           tea
Version:        31.0.0
Release:        1%{?dist}.R
Summary:        TEA text editor

License:        GPLv3
URL:            http://tea-editor.sourceforge.net/
Source0:        http://semiletov.ho.ua/%{name}-releases/%{name}-%{version}.tar.bz2

BuildRequires:  qt4-devel
BuildRequires:  aspell-devel
BuildRequires:  hspell-devel

%description
TEA is a text editor with the hundreds of features.

%prep
%setup -q


%build
qmake-qt4 PREFIX=$RPM_BUILD_ROOT/%{_bindir}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install


%files
%{_bindir}/tea
%doc AUTHORS COPYING ChangeLog README



%changelog
* Wed Sep 21 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 31.0.0-1.R
- Initial release
