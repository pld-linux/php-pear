Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.0
Release:	4
Epoch:		4
License:	Public Domain
Group:		Development/Languages/PHP
Requires:	php-pcre
Requires:	php-xml
Obsoletes:	php-pear-additional_classes
Obsoletes:	php4-pear
Provides:	php4-pear = %{epoch}:%{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/pear

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
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/data

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{php_pear_dir}
%{php_pear_dir}/Archive
%{php_pear_dir}/Console
%{php_pear_dir}/Crypt
%{php_pear_dir}/HTML
%{php_pear_dir}/HTML/Template
%{php_pear_dir}/HTTP
%{php_pear_dir}/Image
%{php_pear_dir}/Math
%{php_pear_dir}/Net
%{php_pear_dir}/Numbers
%{php_pear_dir}/PEAR
%{php_pear_dir}/Science
%{php_pear_dir}/Services
%{php_pear_dir}/Text
%{php_pear_dir}/XML
%{php_pear_dir}/Validate
%{php_pear_dir}/Validate/Finance
EOF

# registry
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{php_pear_dir}/.registry}
> $RPM_BUILD_ROOT%{php_pear_dir}/.filemap
> $RPM_BUILD_ROOT%{php_pear_dir}/.lock

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}
%dir %{php_pear_dir}/Archive
%dir %{php_pear_dir}/Console
%dir %{php_pear_dir}/Crypt
%dir %{php_pear_dir}/HTML
%dir %{php_pear_dir}/HTML/Template
%dir %{php_pear_dir}/HTTP
%dir %{php_pear_dir}/Image
%dir %{php_pear_dir}/Math
%dir %{php_pear_dir}/Net
%dir %{php_pear_dir}/Numbers
%dir %{php_pear_dir}/PEAR
%dir %{php_pear_dir}/Science
%dir %{php_pear_dir}/Services
%dir %{php_pear_dir}/Text
%dir %{php_pear_dir}/XML
%dir %{php_pear_dir}/Validate
%dir %{php_pear_dir}/Validate/Finance

%dir %{php_pear_dir}/data

# registry
%dir %{php_pear_dir}/.registry
%ghost %{php_pear_dir}/.filemap
%ghost %{php_pear_dir}/.lock
