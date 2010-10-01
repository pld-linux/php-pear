#!/bin/sh
urls="
	http://pear.firephp.org/channel.xml
	http://pear.phing.info/channel.xml
	http://pear.phpdb.org/channel.xml
	http://phpseclib.sourceforge.net/channel.xml
	http://pear.phpunit.de/channel.xml
	http://pear.symfony-project.com/channel.xml
	http://pear.roundcube.net/channel.xml
"
for url in $urls; do
	wget -q -O tmp.xml $url || continue
	alias=$(sed -nre 's,.*<suggestedalias>(.+)</suggestedalias>.*$,\1,p' tmp.xml)
	mv -f tmp.xml channel-$alias.xml
done

rm -f tmp.xml
