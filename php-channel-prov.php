#!/usr/bin/php
<?php
# Scan files from .channels dir ending with .reg extension for PEAR channel info
# Author: Elan Ruusamäe <glen@pld-linux.org>
#
# Date: 2010-03-10
# $Id$

if ($argc > 1) {
    $files = array_splice($argv, 1);
} else {
    $files = explode(PHP_EOL, trim(file_get_contents('php://stdin')));
}

foreach ($files as $file) {
	if (strstr($file, '.channels') && substr($file, -4) == '.reg') {
		$reg = unserialize(file_get_contents($file));
		printf("Provides: php-channel(%s)\n", $reg['name']);
	}
}
