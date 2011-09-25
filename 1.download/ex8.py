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
    formatter = "%r %r %r %r"

    print formatter % (1, 2, 3, 4)
    print formatter % ("one", "two", "three", "four")
    print formatter % (True, False, False, True)
    print formatter % (formatter, formatter, formatter, formatter)
    print formatter % (
            "I had this thing.",
            "That you could type up right.",
            "But it didn't sing.",
            "So I said goodnight."
            )

    print 'Done'

if __name__ == '__main__':
    main()
