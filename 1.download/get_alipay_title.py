#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''下载支付宝首页title
'''

import os
import sys
import urllib

def download_title():
    fp = urllib.urlopen("http://www.alipay.com")
    content = fp.read().decode('gb18030')
    fp.close()
    front = content.find('<title>')
    if front < 0:
        return None
    front += 7

    back = content.find('</title>')
    if back < front:
        return None

    expcontent = content[front:back]

    print expcontent

def main():
    ''' main function
    '''
    download_title()

    print 'Done'

if __name__ == '__main__':
    main()
