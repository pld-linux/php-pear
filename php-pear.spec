Summary:	PEAR - PHP Extension and Application Repository
Summary(pl):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.0
Release:	7
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

%description
PEAR - PHP Extension and Application Repository.

Please note that this package provides only basic directory structure.
If you want to use base PEAR classes (PEAR.php, PEAR/*.php), that come
with PHP, please install appropriate php-pear-* (php-pear-PEAR,
php-PEAR-Archive_Tar, etc) packages.

%description -l pl
PEAR (PHP Extension and Application Repository) - rozszerzenie PHP i
repozytorium aplikacji.

Nale�y pami�ta�, �e ten pakiet dostarcza tylko podstawow� struktur�
katalog�w. Aby u�y� podstawowych klas PEAR (PEAR.php PEAR/*.php),
dostarczanych z PHP, nale�y zainstalowa� odpowiednie pakiety
php-pear-* (php-pear-PEAR, php-pear-Archive_Tar, itp).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{data,tests}

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{php_pear_dir}/Archive
%{php_pear_dir}/Console
%{php_pear_dir}/Crypt
%{php_pear_dir}/Contact
%{php_pear_dir}/HTML
%{php_pear_dir}/HTML/Template
%{php_pear_dir}/HTTP
%{php_pear_dir}/Image
%{php_pear_dir}/Math
%{php_pear_dir}/MP3
%{php_pear_dir}/Net
%{php_pear_dir}/Numbers
%{php_pear_dir}/PEAR
%{php_pear_dir}/PHP
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

%post
umask 002
if [ ! -e %{php_pear_dir}/.filemap ]; then
	touch %{php_pear_dir}/.filemap
fi
if [ ! -e %{php_pear_dir}/.lock ]; then
	touch %{php_pear_dir}/.lock
fi

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}
# LANG=C is in 'prep', so this should work in locales like et_EE where [a-z] does not specify whole alphabet
%{php_pear_dir}/[A-Z]*

# see 'pear config-show'
%dir %{php_pear_dir}/data
%dir %{php_pear_dir}/tests

# registry
%dir %{php_pear_dir}/.registry
%ghost %{php_pear_dir}/.filemap
%ghost %{php_pear_dir}/.lock
