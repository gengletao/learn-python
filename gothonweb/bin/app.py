#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''
'''

import web

urls = (
        '/', 'index',
        '/(.*)', 'hello'
        )

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = "Hello World"
        # return render.index(greeting = greeting)
        return render.foo()

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
        
if __name__ == "__main__":
    app.run()
