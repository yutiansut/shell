
from core.CoreHandler import CoreHandler
import json 
from lib.Db import Db

import hashlib

class LoginHandler(CoreHandler):

    def get(self):
        self.render("login.html")

    def post(self):
        try: 
            username = password = None 
            username = self.get_argument("username", "") 
            password = self.get_argument("password", "") 
            if username == None or username == "":
                raise Exception("用户名必须填写")
            elif password == None or password == "":
                raise Exception("用户密码必须填写")

            m = hashlib.sha256()
            m.update(password.encode(encoding="utf-8"))
            hash_password = m.hexdigest()

            db = Db()
            userInfo = db.where("username", username).first()
            print(userInfo)
            
        except Exception as err:
            print(err)


