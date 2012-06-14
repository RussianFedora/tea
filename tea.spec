Name:           tea
Version:        33.1.0
Release:        1%{?dist}
Summary:        TEA text editor

License:        GPLv3
URL:            http://tea-editor.sourceforge.net/
Source0:        http://semiletov.ho.ua/%{name}-releases/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop

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
install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
make install

%post
update-desktop-database -q


%files
%{_bindir}/tea
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/applications/%{name}.desktop


%changelog
* Thu Jun 14 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 33.1.0-1.R
- Update to 33.1.0

* Wed Sep 21 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 31.0.0-1.R
- Initial release
