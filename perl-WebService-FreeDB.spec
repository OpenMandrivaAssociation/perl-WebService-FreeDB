%define upstream_name	 WebService-FreeDB
%define upstream_version 0.77

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	FreeDB search by keyword	
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
WebService-FreeDB is a perl module for retrieving entries from FreeDB 
by searching for keywords (artist,track,album,rest) 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
# make test

%install
%makeinstall_std 

%files
%doc README Changes example/cdsearch.pl
%{_mandir}/man3/*
%{perl_vendorlib}/WebService


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.770.0-1mdv2010.0
+ Revision: 401917
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.77-5mdv2009.0
+ Revision: 258786
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.77-4mdv2009.0
+ Revision: 246703
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.77-2mdv2008.1
+ Revision: 171033
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.77-1mdv2008.0
+ Revision: 23230
- disable test, don't work on the cluster


* Tue Jun 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.76-1mdv2007.0
- New version 0.76

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-1mdk
- New release 0.73

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.1-2mdk
- Fix BuildRequires

* Thu Jun 16 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.1-1mdk
- 0.7.1
- %%mkrel
- Make Rpmbuildupdate happy
- Fix URL
- Drop Patch 0 ( Merged Upstream )

* Wed Jun 08 2005 Stew Benedict <sbenedict@mandriva.com> 0.7-2mdk
- rebuild for new perl, patch for new page layout (P0)

* Sun Apr 24 2005 Stew Benedict <sbenedict@mandriva.com> 0.7-1mdk
- first Mandriva release

