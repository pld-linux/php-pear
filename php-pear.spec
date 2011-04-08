Summary:	PEAR - PHP Extension and Application Repository
Summary(pl.UTF-8):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.3.5
Release:	3
Epoch:		4
License:	Public Domain
Group:		Development/Languages/PHP
Source0:	php-channel-prov.php
Source100:	update-channels.sh
Source1:	channel-phing.xml
Source2:	channel-phpdb.xml
Source3:	channel-firephp.xml
Source4:	channel-symfony.xml
Source5:	channel-phpunit.xml
Source6:	channel-phpseclib.xml
Source7:	channel-horde.xml
Source8:	channel-rc.xml
Source9:	channel-ezc.xml
Source10:	channel-propel.xml
BuildRequires:	/usr/bin/php
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpmbuild(macros) >= 1.570
Obsoletes:	php-pear-additional_classes
Obsoletes:	php4-pear
Conflicts:	php-pear-PEAR < 1:1.7.2-10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__reg_provides	php %{SOURCE0}

# find channel provides
%define		_use_internal_dependency_generator 0
%define		__find_provides %{__reg_provides}
%define		__find_requires %{nil}

# avoid rpm 4.4.9 adding rm -rf buildroot, we need the dirs to check consistency
%define		__spec_clean_body	%{nil}

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
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{.registry,bin,data,tests}

# add extra channels
%{__pear} -c pearrc config-set php_dir $RPM_BUILD_ROOT%{php_pear_dir}
for xml in $(awk '/^Source[0-9]+:.+channel-.+.xml$/ {print $NF}' %{_specdir}/%{name}.spec); do
	%{__pear} -c pearrc channel-add %{_sourcedir}/$xml
done

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
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
%{php_pear_dir}/Mail
%{php_pear_dir}/Math
%{php_pear_dir}/Net
%{php_pear_dir}/Net/UserAgent
%{php_pear_dir}/Numbers
%{php_pear_dir}/PHP
%{php_pear_dir}/Payment
%{php_pear_dir}/QA
%{php_pear_dir}/Science
%{php_pear_dir}/Services
%{php_pear_dir}/Structures
%{php_pear_dir}/Testing
%{php_pear_dir}/Text
%{php_pear_dir}/Text/CAPTCHA
%{php_pear_dir}/Text/Spell
%{php_pear_dir}/URI
%{php_pear_dir}/Validate
%{php_pear_dir}/Validate/Finance
%{php_pear_dir}/VersionControl
%{php_pear_dir}/XML
EOF

%clean
cd $RPM_BUILD_ROOT%{php_pear_dir}

check_channel_dirs() {
	RPMFILE=%{name}-%{version}-%{release}.%{_target_cpu}.rpm
	TMPFILE=$(mktemp)
	find .channels .registry -type d | LC_ALL=C sort > $TMPFILE

	# find finds also '.', so use option -B for diff
	if rpm -qplv %{_rpmdir}/$RPMFILE | sed -ne '/^d/s,^.*%{php_pear_dir}/\.,.,p' | LC_ALL=C sort | diff -uB $TMPFILE - ; then
		rm -rf $RPM_BUILD_ROOT
	else
		echo -e "\nNot so good, some channel directories are not included in package\n"
		exit 1
	fi
	rm -f $TMPFILE
}
check_channel_dirs

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}
%{php_pear_dir}/*

%ghost %{php_pear_dir}/.depdblock
%ghost %{php_pear_dir}/.depdb
%ghost %{php_pear_dir}/.filemap
%ghost %{php_pear_dir}/.lock

%dir %{php_pear_dir}/.registry
%dir %{php_pear_dir}/.channels
%dir %{php_pear_dir}/.channels/.alias

# core channels
%{php_pear_dir}/.channels/__uri.reg
%{php_pear_dir}/.registry/.channel.__uri

%{php_pear_dir}/.channels/.alias/pear.txt
%{php_pear_dir}/.channels/pear.php.net.reg

%{php_pear_dir}/.channels/.alias/pecl.txt
%{php_pear_dir}/.channels/pecl.php.net.reg
%{php_pear_dir}/.registry/.channel.pecl.php.net

%{php_pear_dir}/.channels/.alias/phpdocs.txt
%{php_pear_dir}/.channels/doc.php.net.reg
%{php_pear_dir}/.registry/.channel.doc.php.net

# addon channels
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
%{php_pear_dir}/.registry/.channel.pear.firephp.org

%{php_pear_dir}/.channels/.alias/symfony.txt
%{php_pear_dir}/.channels/pear.symfony-project.com.reg
%{php_pear_dir}/.registry/.channel.pear.symfony-project.com

%{php_pear_dir}/.channels/.alias/phpseclib.txt
%{php_pear_dir}/.channels/phpseclib.sourceforge.net.reg
%{php_pear_dir}/.registry/.channel.phpseclib.sourceforge.net

%{php_pear_dir}/.channels/.alias/horde.txt
%{php_pear_dir}/.channels/pear.horde.org.reg
%{php_pear_dir}/.registry/.channel.pear.horde.org

%{php_pear_dir}/.channels/.alias/rc.txt
%{php_pear_dir}/.channels/pear.roundcube.net.reg
%{php_pear_dir}/.registry/.channel.pear.roundcube.net

%{php_pear_dir}/.channels/.alias/ezc.txt
%{php_pear_dir}/.channels/components.ez.no.reg
%{php_pear_dir}/.registry/.channel.components.ez.no

%{php_pear_dir}/.channels/.alias/propel.txt
%{php_pear_dir}/.channels/pear.propelorm.org.reg
%{php_pear_dir}/.registry/.channel.pear.propelorm.org
