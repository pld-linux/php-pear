Summary:	PEAR - PHP Extension and Application Repository
Summary(pl.UTF-8):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.2
Release:	1
Epoch:		4
License:	Public Domain
Group:		Development/Languages/PHP
Source0:	channel-phpunit.xml
Source1:	channel-phing.xml
Source2:	channel-phpdb.xml
Source3:	channel-firephp.xml
Source10:	php-channel-prov.php
BuildRequires:	/usr/bin/php
BuildRequires:	php-pear-PEAR
Obsoletes:	php-pear-additional_classes
Obsoletes:	php4-pear
Conflicts:	php-pear-PEAR < 1:1.4.6-1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_registrydir	%{php_pear_dir}/.registry

%define		__reg_provides	php %{SOURCE10}

%define		_use_internal_dependency_generator 0
%define		__find_provides %{__reg_provides}
%define		__find_requires %{nil}

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
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{bin,data,tests}

# add extra channels
pear -c pearrc config-set php_dir $RPM_BUILD_ROOT%{php_pear_dir}
pear -c pearrc channel-add %{SOURCE0}
pear -c pearrc channel-add %{SOURCE1}
pear -c pearrc channel-add %{SOURCE2}
pear -c pearrc channel-add %{SOURCE3}

rm -f $RPM_BUILD_ROOT%{php_pear_dir}/.channels/.alias/{pear,pecl}.txt
rm -f $RPM_BUILD_ROOT%{php_pear_dir}/.channels/__uri.reg
rm -f $RPM_BUILD_ROOT%{php_pear_dir}/.channels/{pear,pecl}.php.net.reg
rm -f $RPM_BUILD_ROOT%{php_pear_dir}/{.depdb*,.filemap,.lock}

# TODO:
install -d $RPM_BUILD_ROOT%{_registrydir}/.channel.pear.phpdb.org

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{php_pear_dir}/.registry
%{php_pear_dir}/bin
%{php_pear_dir}/Archive
%{php_pear_dir}/Auth
%{php_pear_dir}/Cache
%{php_pear_dir}/Console
%{php_pear_dir}/Contact
%{php_pear_dir}/Crypt
%{php_pear_dir}/DB/DataObject
%{php_pear_dir}/Event
%{php_pear_dir}/File
%{php_pear_dir}/Genealogy
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
%dir %{php_pear_dir}
%{php_pear_dir}/*

%dir %{php_pear_dir}/.registry
%dir %{php_pear_dir}/.channels
%dir %{php_pear_dir}/.channels/.alias

%{php_pear_dir}/.channels/.alias/phpunit.txt
%{php_pear_dir}/.channels/pear.phpunit.de.reg
%{php_pear_dir}/.registry/.channel.pear.phpunit.de

%{php_pear_dir}/.channels/.alias/phing.txt
%{php_pear_dir}/.channels/pear.phing.info.reg
%{php_pear_dir}/.registry/.channel.pear.phing.info

%{php_pear_dir}/.channels/.alias/phpdb.txt
%{php_pear_dir}/.channels/pear.phpdb.org.reg
%{php_pear_dir}/.registry/.channel.pear.phpdb.org

%{php_pear_dir}/.channels/.alias/firephp.txt
%{php_pear_dir}/.channels/pear.firephp.org.reg
