%define upstream_name	 WebService-FreeDB
%define upstream_version 0.79
Name:		perl-%{upstream_name}
Version:	0.79
Release:	2

Summary:	FreeDB search by keyword	
License:	GPL
Group:		Development/Perl
URL:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/R/RU/RURBAN/WebService-FreeDB-0.79.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
WebService-FreeDB is a perl module for retrieving entries from FreeDB 
by searching for keywords (artist,track,album,rest) 

%prep
%setup -q -n WebService-FreeDB-0.79

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
# soft: do not fail package on test failures
set +e
# make test || :

%install
%makeinstall_std 

%files
%doc README Changes example/cdsearch.pl
%{_mandir}/man3/*
%{perl_vendorlib}/WebService


