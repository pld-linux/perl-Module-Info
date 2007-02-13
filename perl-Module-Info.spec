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
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Vendor:		Mattia Barbon <MBARBON@cpan.org>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1e4e39cceda93dc0ab2d296b5075d76
%if %{with tests}
#BuildRequires:	perl-B-Utils
BuildRequires:	perl(File::Spec) >= 0.8
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	perl-B-Utils
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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/B/*.pm
%{perl_vendorlib}/B/Module
%{perl_vendorlib}/Module/Info.pm
%{_mandir}/man[13]/*
