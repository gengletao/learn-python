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
    cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

    cities['NY'] = 'New York'
    cities['OR'] = 'Portland'

    def find_city(themap, state):
        if state in themap:
            return themap[state]
        else:
            return "Not found."

    # ok pay attention!
    cities['_find'] = find_city

    while True:
        print "State? (ENTER to quite)",
        state = raw_input("> ")

        if not state:break

        # this line is the most important ever! study!
        city_found = cities['_find'](cities, state)
        print city_found

    print 'Done'

if __name__ == '__main__':
    main()
