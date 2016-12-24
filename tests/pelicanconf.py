#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# pylint: disable=missing-docstring

from __future__ import unicode_literals

AUTHOR = u'Test'
SITEURL = u''
SITENAME = u"Test Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Test'
SITEDESCRIPTION = u'%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = u'https://www.example.com/img/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'
BROWSER_COLOR = '#333'

ROBOTS = u'index, follow'

THEME = u'./themes/simple/'
PATH = u'content'
TIMEZONE = u'Europe/Sofia'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

LINKS = (('Mr. Senko', 'http://MrSenko.com'),)

SOCIAL = (('twitter', 'https://twitter.com/MrSenko'),
          ('github', 'https://github.com/MrSenko'))

MENUITEMS = ()

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

PLUGIN_PATHS = ['../']
PLUGINS = ['pelican_ab']
