#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My First Project',
        'author': 'letao geng',
        'url': 'url',
        'download_url': 'download_url',
        'author_email': 'gengletao@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'scripts': [],
        'name': 'firstproject'
        }

setup(**config)
