#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'Team Brawndo'
SITENAME = u'CBBS Imaging Docs'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican-page-hierarchy', 'pelican-toc', 'tipue_search', 'headerid', 'sitemap']
SITEMAP = { 'format': 'xml' }

THEME = 'theme'
DIRECT_TEMPLATES = ['search'] # unset all templates
STATIC_PATHS = ['css', 'ts']

PATH_METADATA = 'pages/(?P<path>.*)\..*'
PAGE_ORDER_BY = 'order'
TOC = { 'TOC_INCLUDE_TITLE': 'false' }
HEADERID_LINK_CHAR = '<i class="icon-link"></i>'

FEED_ALL_ATOM = None
AUTHOR_SAVE_AS = False
