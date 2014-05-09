#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'herlo'
SITENAME = u'NerdLun.ch'
SITESUBTITLE = u'A Community of Nerdy Lunchers'
INDEX_WELCOME = u'Welcome to Nerd Lunch'
SITEURL = 'http://nerdlun.ch'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'

THEME = 'themes/chunk'
LINKS = (('News', 'news.html'), )

INDEX_SAVE_AS = 'index.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

DELETE_OUTPUT_DIRECTORY = True

DISPLAY_CATEGORIES_ON_MENU = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'News'
