#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''
'''

import os
import sys

def main():
    ''' main function
    '''
    # Here's some new strange stuff, remember type it exactly.

    days = "Mon Tue Wed Thu Fri Sat Sun"
    months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"

    print "Here are the days: ", days
    print "Here are the months: ", months
    
    print """
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
    """

    print 'Done'

if __name__ == '__main__':
    main()
