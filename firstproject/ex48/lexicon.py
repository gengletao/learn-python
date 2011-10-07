#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''
'''


def scan(sentence):
    directions = ('north', 'south', 'east', 'west')
    verbs = ('go', 'kill', 'eat')
    stops = ('the', 'in', 'of')
    nouns = ('bear', 'princess')
    
    words = sentence.lower().split(' ')

    result = []
    for word in words:
        if (directions.__contains__(word)):
            result.append(('direction', word))
        elif (verbs.__contains__(word)):
            result.append(('verb', word))
        elif (stops.__contains__(word)):
            result.append(('stop', word))
        elif (nouns.__contains__(word)):
            result.append(('noun', word))
        elif (convert_number(word)):
            result.append(('number', int(word)))
        else:
            result.append(('error', word))

    return result

def convert_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class lexicon(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.word = []
