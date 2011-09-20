#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''下载支付宝首页title
'''

import os
import sys
import urllib

def download_content(url):
    fp = urllib.urlopen(url)
    content = fp.read()
    fp.close()
    return content

def get_expcontent(content,front_split,back_split):
    front = content.find(front_split)
    if front < 0:
        return None
    front += len(front_split)

    back = content.find(back_split)
    if back < front:
        return None

    expcontent = content[front:back]
    return expcontent

def main():
    ''' main function
    '''
    url = 'http://www.alipay.com'
    front_split = '<title>'
    back_split = '</title>'

    content = download_content(url).decode('gb18030')
    expcontent = get_expcontent(content, front_split, back_split)

    print expcontent
    print 'Done'

if __name__ == '__main__':
    main()
