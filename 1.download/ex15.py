#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''
'''

import os
from sys import argv

def main():
    ''' main function
    '''
    script, filename = argv
    
    txt = open(filename)

    print "Here's your file %r" % filename
    print txt.read()

    txt.close()

    print "I'll also ask you to type it again:"
    file_again = raw_input("> ")

    txt_again = open(file_again)
    
    print txt_again.read()

    txt_again.close()

    print 'Done'

if __name__ == '__main__':
    main()
