#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Info
Summary:	Module::Info perl module - information about Perl Modules
Summary(pl):	Modu³ perla Module::Info - informacje o modu³ach perla
Name:		perl-Module-Info
Version:	0.12
Release:	3
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
#BuildRequires:	perl-B-Utils
BuildRequires:	perl(File::Spec) >= 0.8
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
Conflicts:	perl-B-Utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Info gives you information about Perl modules without actually
loading the module. It actually isn't specific to modules and should
work on any perl code.

%description -l pl
Module::Info podaje informacje o modu³ach Perla bez wczytywania
modu³u. Dzia³anie to w³a¶ciwie nie jest ograniczone do modu³ów i
powinno dzia³aæ z dowolnym kodem w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/B/*.pm
%{perl_sitelib}/B/Module
%{perl_sitelib}/Module/Info.pm
%{_mandir}/man[13]/*
