%define module	WebService-FreeDB
%define name	perl-%{module}
%define version 0.77
%define release %mkrel 5 

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	FreeDB search by keyword	
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/WebService/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
WebService-FreeDB is a perl module for retrieving entries from FreeDB 
by searching for keywords (artist,track,album,rest) 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
# %{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std 

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README Changes example/cdsearch.pl
%{_mandir}/man3/*
%{perl_vendorlib}/WebService

