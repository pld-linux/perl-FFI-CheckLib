#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	FFI
%define		pnam	CheckLib
Summary:	FFI::CheckLib - Check that a library is available for FFI
Summary(pl.UTF-8):	FFI::CheckLib - sprawdzanie, czy biblioteka jest dostępna dla FFI
Name:		perl-FFI-CheckLib
Version:	0.31
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/FFI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ffc8e61bb686dd631bed3ddf102af41c
URL:		https://metacpan.org/dist/FFI-CheckLib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Test2::API) >= 1.302015
BuildRequires:	perl-Scalar-List-Utils >= 1.33
BuildRequires:	perl-Test2-Suite >= 0.000121
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module checks whether a particular dynamic library is available
for FFI to use. It is modeled heavily on Devel::CheckLib, but will
find dynamic libraries even when development packages are not
installed. It also provides a find_lib function that will return the
full path to the found dynamic library, which can be feed directly
into FFI::Platypus or another FFI system.

%description -l pl.UTF-8
Ten moduł sprawdza, czy pewna biblioteka dynamiczna jest dostępna do
użycia przez FFI. Jest wzorowana w dużym stopniu na Devel::CheckLib,
ale znajduje biblioteki dynamiczne nawet jeśli pakiety programistyczne
nie są zainstalowane. Udostępnia także funkcję find_lib, zwracającą
pełną ścieżkę do znalezionej biblioteki dynamicznej, którą można
bezpośrednio przekazać do FFI::Platypus lub innego systemu FFI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/FFI
%{perl_vendorlib}/FFI/CheckLib.pm
%{_mandir}/man3/FFI::CheckLib.3pm*
%{_examplesdir}/%{name}-%{version}
