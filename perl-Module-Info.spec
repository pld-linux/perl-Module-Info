#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Info
Summary:	Module::Info perl module - information about Perl modules
Summary(pl.UTF-8):	Moduł perla Module::Info - informacje o modułach Perla
Name:		perl-Module-Info
Version:	0.33
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	422824cc46ba6b571f2319ba1cf5f2f9
URL:		http://search.cpan.org/dist/Module-Info/
%if %{with tests}
#BuildRequires:	perl-B-Utils
BuildRequires:	perl(File::Spec) >= 0.8
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Info gives you information about Perl modules without actually
loading the module. It actually isn't specific to modules and should
work on any perl code.

%description -l pl.UTF-8
Module::Info podaje informacje o modułach Perla bez wczytywania
modułu. Działanie to właściwie nie jest ograniczone do modułów i
powinno działać z dowolnym kodem w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/module_info
%attr(755,root,root) %{_bindir}/pfunc
%{perl_vendorlib}/B/BUtils.pm
%{perl_vendorlib}/B/Module
%{perl_vendorlib}/Module/Info.pm
%{_mandir}/man1/module_info.1p*
%{_mandir}/man1/pfunc.1p*
%{_mandir}/man3/B::BUtils.3pm*
%{_mandir}/man3/B::Module::Info.3pm*
%{_mandir}/man3/Module::Info.3pm*
