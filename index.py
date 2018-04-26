import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os

from configs.rounter import *

from tornado.options import define, options 

define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    rounter = rounterConfig()
    settings = {
            "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            "login_url": "/login",
    }

    app = tornado.web.Application(
            handlers= rounter,  
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), 'resources'),
            debug=True,
            **settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
