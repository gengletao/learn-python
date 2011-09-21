#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

''' operation exercise
'''

import os
import sys

def main():
    ''' main function
    '''
    #start count chicken
    print "I will now count my chickens:"

    #count hen
    print "Hens", 25 + 30.0 / 6
    #count rooster
    print "Roosters", 100 - 25.0 * 3 % 4

    #start count egg
    print "Now I will count the eggs:"

    #count(egg)
    print 3 + 2 + 1 - 5 + 4 % 2 -1.0 / 4 + 6

    #compare two numbers
    print "Is it true that 3.0 + 2 < 5 - 7?"

    print 3.0 + 2 < 5 - 7

    print "What is 3.0 + 2?", 3.0 + 2
    print "What is 5.0 - 7?", 5.0 - 7

    print "Oh, that's why it's False."

    #some other exercise
    print "How about some more."

    print "Is it greater?", 5.0 > -2
    print "Is it greater or equal?", 5.0 >= -2
    print "Is it less or equal?", 5.0 <= -2

    print 'Done'

if __name__ == '__main__':
    main()
