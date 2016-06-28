#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Informationen über ein Video mittels vimeo-API auslesen
# Lizenz: MIT license
# Datum: 09.11.2012
# 

import urllib2
import simplejson

videoid = "52073296"
url = "http://vimeo.com/api/v2/video/" + videoid + ".json"
handle = urllib2.urlopen(url)
content = handle.read()
j = simplejson.loads(content)

for key in j[0]:
	print "{0}: {1}".format(key,j[0][key])
