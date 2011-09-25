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
    x = "There are %d types of people." % 10
    binary = "binary"
    do_not = "don't"
    y = "Those who know %s and those who %s." % (binary, do_not)

    print x
    print y
    print "I said: %r." % x
    print "I also said: '%s'." % y

    hilarious = False
    joke_evaluation = "Isn't that joke so funny?! %r"
    
    print joke_evaluation % hilarious

    w = "This is the Left side of..."
    e = "a string with a right side."
    print w + e

    print 'Done'

if __name__ == '__main__':
    main()
