#!/bin/sh
channels="
	components.ez.no
	pear.docblox-project.org
	pear.firephp.org
	pear.horde.org
	pear.indeyets.ru
	pear.michelf.com
	pear.netpirates.net
	pear.pdepend.org
	pear.phing.info
	pear.phpdb.org
	pear.phpdoc.org
	pear.phpmd.org
	pear.phpunit.de
	pear.propelorm.org
	pear.roundcube.net
	pear.symfony-project.com
	pear.symfony.com
	pear.twig-project.org
	phpseclib.sourceforge.net
	saucelabs.github.com/pear
	zustellzentrum.cweiske.de
"
for channel in ${@:-$channels}; do
	url=http://$channel/channel.xml
	wget -q --timeout=10 --tries=1 -O tmp.xml $url || continue
	alias=$(sed -nre 's,.*<suggestedalias>(.+)</suggestedalias>.*$,\1,p' tmp.xml)
	sed -i -e 's,\r$,,g; s,\r,\n,g' tmp.xml
	mv -f tmp.xml channel-$alias.xml
done

rm -f tmp.xml
