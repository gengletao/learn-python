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
    print "How old are you?",
    age = raw_input()
    print "How tall are you?",
    height = raw_input()
    print "How much do you weight?",
    weight = raw_input()

    print "So, you're %r old, %r tall and %r heavy." % (
            age, height, weight)

    print 'Done'

if __name__ == '__main__':
    main()
