%define upstream_name	 WebService-FreeDB
%define upstream_version 0.77

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	FreeDB search by keyword	
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
WebService-FreeDB is a perl module for retrieving entries from FreeDB 
by searching for keywords (artist,track,album,rest) 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
