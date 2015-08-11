Summary:	PEAR - PHP Extension and Application Repository
Summary(pl.UTF-8):	PEAR - rozszerzenie PHP i repozytorium aplikacji
Name:		php-pear
Version:	1.3.17
Release:	1
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
Source11:	channel-docblox.xml
Source12:	channel-michelf.xml
Source13:	channel-phpmd.xml
Source14:	channel-pdepend.xml
Source15:	channel-symfony2.xml
Source16:	channel-saucelabs.xml
Source17:	channel-twig.xml
Source18:	channel-zz.xml
Source19:	channel-theseer.xml
Source20:	channel-indeyets.xml
Source21:	channel-phpdoc.xml
Source22:	channel-bartlett.xml
BuildRequires:	/usr/bin/php
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpmbuild(macros) >= 1.570
Obsoletes:	php-pear-additional_classes
Obsoletes:	php4-pear
Conflicts:	php-pear-PEAR < 1:1.7.2-10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__reg_provides	%{__php} %{SOURCE0}

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

%build
rm -rf pear
install -d pear

# add extra channels
%{__pear} -c pearrc config-set php_dir pear
for xml in $(awk '/^Source[0-9]+:.+channel-.+.xml$/ {print $NF}' %{_specdir}/%{name}.spec); do
	%{__pear} -c pearrc channel-add %{_sourcedir}/$xml
done

%install
install -d $RPM_BUILD_ROOT%{php_pear_dir}/{.registry,bin,data,tests}
cp -a pear/.??* $RPM_BUILD_ROOT%{php_pear_dir}

while read dir; do
	install -d $RPM_BUILD_ROOT$dir
done <<EOF
%{php_pear_dir}/Archive
%{php_pear_dir}/Auth
%{php_pear_dir}/Cache
%{php_pear_dir}/Console
%{php_pear_dir}/Contact
%{php_pear_dir}/Crypt
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
%{php_pear_dir}/Horde
%{php_pear_dir}/Horde/Stream
%{php_pear_dir}/Horde/Text
%{php_pear_dir}/Horde/Xml
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
%{php_pear_dir}/SebastianBergmann
%{php_pear_dir}/Services
%{php_pear_dir}/Structures
%{php_pear_dir}/Symfony
%{php_pear_dir}/Symfony/Bridge
%{php_pear_dir}/Symfony/Component
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
check_channel_dirs() {
	local RPMFILE=%{name}-%{version}-%{release}.%{_target_cpu}.rpm
	local installed=$(mktemp -t instXXXXXX.tmp)
	local rpmfiles=$(mktemp -t rpmXXXXXX.tmp)
	local rc diff=$(mktemp -t diffXXXXXX.tmp)

	find $RPM_BUILD_ROOT%{php_pear_dir} | LC_ALL=C sort > $installed
	sed -i -re "s#^$RPM_BUILD_ROOT%{php_pear_dir}/?##" $installed

	rpm -qpl %{_rpmdir}/$RPMFILE |  LC_ALL=C sort > $rpmfiles
	sed -i -re "s#^%{php_pear_dir}/?##" $rpmfiles

	# find finds also '.', so use option -B for diff
	if ! diff -uB $installed $rpmfiles > $diff; then
		cat <<-EOF

		ERROR: some files/directories are not included in package:

		$(%{__sed} -ne '/^-[^-]/ s#^-#%%{php_pear_dir}/#p' $diff)

		EOF

		exit 1
	fi
	rm -rf $RPM_BUILD_ROOT
	rm -f $installed $rpmfiles $diff
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

%{php_pear_dir}/.channels/.alias/docblox.txt
%{php_pear_dir}/.channels/pear.docblox-project.org.reg
%{php_pear_dir}/.registry/.channel.pear.docblox-project.org

%{php_pear_dir}/.channels/.alias/michelf.txt
%{php_pear_dir}/.channels/pear.michelf.com.reg
%{php_pear_dir}/.registry/.channel.pear.michelf.com

%{php_pear_dir}/.channels/.alias/pdepend.txt
%{php_pear_dir}/.channels/pear.pdepend.org.reg
%{php_pear_dir}/.registry/.channel.pear.pdepend.org

%{php_pear_dir}/.channels/.alias/phpmd.txt
%{php_pear_dir}/.channels/pear.phpmd.org.reg
%{php_pear_dir}/.registry/.channel.pear.phpmd.org

%{php_pear_dir}/.channels/.alias/symfony2.txt
%{php_pear_dir}/.channels/pear.symfony.com.reg
%{php_pear_dir}/.registry/.channel.pear.symfony.com

%{php_pear_dir}/.channels/.alias/saucelabs.txt
%{php_pear_dir}/.channels/saucelabs.github.com_pear.reg
%{php_pear_dir}/.registry/.channel.saucelabs.github.com_pear

%{php_pear_dir}/.channels/.alias/twig.txt
%{php_pear_dir}/.channels/pear.twig-project.org.reg
%{php_pear_dir}/.registry/.channel.pear.twig-project.org

%{php_pear_dir}/.channels/.alias/zz.txt
%{php_pear_dir}/.channels/zustellzentrum.cweiske.de.reg
%{php_pear_dir}/.registry/.channel.zustellzentrum.cweiske.de

%{php_pear_dir}/.channels/.alias/theseer.txt
%{php_pear_dir}/.channels/pear.netpirates.net.reg
%{php_pear_dir}/.registry/.channel.pear.netpirates.net

%{php_pear_dir}/.channels/.alias/indeyets.txt
%{php_pear_dir}/.channels/pear.indeyets.ru.reg
%{php_pear_dir}/.registry/.channel.pear.indeyets.ru

%{php_pear_dir}/.channels/.alias/phpdoc.txt
%{php_pear_dir}/.channels/pear.phpdoc.org.reg
%{php_pear_dir}/.registry/.channel.pear.phpdoc.org

%{php_pear_dir}/.channels/.alias/bartlett.txt
%{php_pear_dir}/.channels/bartlett.laurent-laville.org.reg
%{php_pear_dir}/.registry/.channel.bartlett.laurent-laville.org
