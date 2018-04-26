#!/usr/bin/env python
# encoding: utf-8

from core.CoreHandler import CoreHandler
import tornado.web

class MainHandler(CoreHandler):

    @tornado.web.authenticated
    def get(self): 
        #self.render("index.html")
        self.write("Hello, world2")

