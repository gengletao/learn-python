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
    age = raw_input("How old are you? ")
    height = raw_input("How tall are you? ")
    weight = raw_input("How much do you weight? ")

    print "So, you're %r old, %r tall and %r heavy." % (
            age, height, weight)

    print 'Done'

if __name__ == '__main__':
    main()
