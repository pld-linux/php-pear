#!/bin/sh
channels="
	components.ez.no
	pear.firephp.org
	pear.phing.info
	pear.phpdb.org
	pear.phpunit.de
	pear.roundcube.net
	pear.symfony-project.com
	phpseclib.sourceforge.net
"
for channel in $channels; do
	url=http://$channel/channel.xml
	wget -q -O tmp.xml $url || continue
	alias=$(sed -nre 's,.*<suggestedalias>(.+)</suggestedalias>.*$,\1,p' tmp.xml)
	mv -f tmp.xml channel-$alias.xml
done

rm -f tmp.xml
