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

fetch() {
	local url="$1"
	local target="$2"
	wget -q --timeout=10 --tries=1 ${target:+-O "$target"} "$url"
}

for channel in ${@:-$channels}; do
	url=http://$channel/channel.xml
	fetch $url tmp.xml  || continue
	alias=$(sed -nre 's,.*<suggestedalias>(.+)</suggestedalias>.*$,\1,p' tmp.xml)
	sed -i -e 's,\r$,,g; s,\r,\n,g' tmp.xml
	mv -f tmp.xml channel-$alias.xml

	url=http://$channel/feed.xml
	fetch $url tmp.xml  || continue
	mv -f tmp.xml feed-$alias.xml
done

rm -f tmp.xml
