#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: letao geng <gengletao@gmail.com>
# Copyright (C) alipay.com 2011

'''
'''

import web

urls = (
        '/hello', 'Index',
        '/(.*)', 'hello'
        )

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

'''
class Index(object):
    def GET(self):
        form = web.input(name = "Nobody", greet = None)

        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting)
            # return render.foo()
        else:
            return "ERROR: greet is required."
'''

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
        
if __name__ == "__main__":
    app.run()
