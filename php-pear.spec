Summary:	PEAR - PHP Extension and Application Repository
Summary(pl.UTF-8):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.0
Release:	23
Epoch:		4
License:	Public Domain
Group:		Development/Languages/PHP
Obsoletes:	php-pear-additional_classes
Obsoletes:	php4-pear
Conflicts:	php-pear-PEAR < 1:1.4.6-1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEAR - PHP Extension and Application Repository.

Please note that this package provides only basic directory structure.
If you want to use base PEAR classes (PEAR.php, PEAR/*.php), that come
with PHP, please install appropriate php-pear-* (php-pear-PEAR,
php-PEAR-Archive_Tar, etc) packages.

%description -l pl.UTF-8
PEAR (PHP Extension and Application Repository) - rozszerzenie PHP i
repozytorium aplikacji.

Należy pamiętać, że ten pakiet dostarcza tylko podstawową strukturę
katalogów. Aby użyć podstawowych klas PEAR (PEAR.php PEAR/*.php),
dostarczanych z PHP, należy zainstalować odpowiednie pakiety
php-pear-* (php-pear-PEAR, php-pear-Archive_Tar, itp).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{data,tests}

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{php_pear_dir}/.registry
%{php_pear_dir}/Archive
%{php_pear_dir}/Auth
%{php_pear_dir}/Cache
%{php_pear_dir}/Console
%{php_pear_dir}/Contact
%{php_pear_dir}/Crypt
%{php_pear_dir}/DB/DataObject
%{php_pear_dir}/File
%{php_pear_dir}/Gtk
%{php_pear_dir}/Gtk2
%{php_pear_dir}/HTML
%{php_pear_dir}/HTML/QuickForm
%{php_pear_dir}/HTML/Table
%{php_pear_dir}/HTML/Template
%{php_pear_dir}/HTTP
%{php_pear_dir}/HTTP/WebDAV
%{php_pear_dir}/HTTP/WebDAV/Tools
%{php_pear_dir}/I18N
%{php_pear_dir}/Image
%{php_pear_dir}/MP3
%{php_pear_dir}/Math
%{php_pear_dir}/Net
%{php_pear_dir}/Numbers
%{php_pear_dir}/PHP
%{php_pear_dir}/Payment
%{php_pear_dir}/QA
%{php_pear_dir}/Science
%{php_pear_dir}/Services
%{php_pear_dir}/Structures
%{php_pear_dir}/Testing
%{php_pear_dir}/Text
%{php_pear_dir}/Text/Spell
%{php_pear_dir}/URI
%{php_pear_dir}/Validate
%{php_pear_dir}/Validate/Finance
%{php_pear_dir}/VersionControl
%{php_pear_dir}/XML
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}
