Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.0
Release:	2
Epoch:		4
License:	Public Domain
Group:		Development/Languages/PHP
Requires:	php-pcre
Requires:	php-xml
Provides:	php4-pear
Obsoletes:	php-pear-additional_classes
Obsoletes:	php4-pear
Provides:	php4-pear = %{epoch}:%{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEAR - PHP Extension and Application Repository.

Please note that this package provides only basic directory structure.
If you want to use base PEAR classes (PEAR.php, PEAR/*.php), that come
with PHP, please install appropriate php-pear-* (php-pear-PEAR,
php-PEAR-Archive_Tar, etc) packages.

%description -l pl
PEAR (PHP Extension and Application Repository) - rozszerzenie PHP i
repozytorium aplikacji.

Nale¿y pamiêtaæ, ¿e ten pakiet dostarcza tylko podstawow± strukturê
katalogów. Aby u¿yæ podstawowych klas PEAR (PEAR.php PEAR/*.php),
dostarczanych z PHP, nale¿y zainstalowaæ odpowiednie pakiety
php-pear-* (php-pear-PEAR, php-pear-Archive_Tar, itp).

%prep

%install
# Directories created for pear:
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{Archive,Console,Crypt,HTML/Template,HTTP,Image,Math,Net,PEAR,Science,Services,Text,XML}

%files
%defattr(644,root,root,755)
%{php_pear_dir}
