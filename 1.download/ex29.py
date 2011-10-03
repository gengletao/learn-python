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
    people = 20
    cats = 30
    dogs = 15

    if people < cats:
        print "Too many cats! The world is doomed!"

    if people > cats:
        print "Not many cats! The world is saved!"

    if people < dogs:
        print "The world is drooled on!"

    if people > dogs:
        print "The world is dry!"

    dogs += 5

    if people >= dogs:
        print "People are greater than or equal to dogs."

    if people <= dogs:
        print "People are less than or equal to dogs."

    if people == dogs:
        print "People are equal to dogs."

    print 'Done'

if __name__ == '__main__':
    main()
