
"""
控制器父类
"""
import requests

import tornado.web

class CoreHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")


        
