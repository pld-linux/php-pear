#!/bin/sh
channels="
	pear.firephp.org
	pear.phing.info
	pear.phpdb.org
	phpseclib.sourceforge.net
	pear.phpunit.de
	pear.symfony-project.com
	pear.roundcube.net
	components.ez.no
"
for channel in $channels; do
	url=http://$channel/channel.xml
	wget -q -O tmp.xml $url || continue
	alias=$(sed -nre 's,.*<suggestedalias>(.+)</suggestedalias>.*$,\1,p' tmp.xml)
	mv -f tmp.xml channel-$alias.xml
done

rm -f tmp.xml
