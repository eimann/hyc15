#!/usr/bin/env python

import os.path
import logging
import uuid
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class IdHandler(tornado.web.RequestHandler):
    def get(self):
        message = {
            "id": str(uuid.uuid4()),
        } 

class ColorHandler(tornado.web.RequestHandler):
    def post(self):
        data_json = tornado.escape.json_decode(self.request.body)
        #FIXME this is somehow broken
        #message = {
        #    "id": str(uuid.uuid4()),
        #    "color": self.post_argument("color"),
        #}
        # to_basestring is necessary for Python 3's json encoder,
        # which doesn't accept byte strings.
        #message = tornado.escape.to_basestring(
        #self.write(color))

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/GetId", IdHandler),
        (r"/SetColor", ColorHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': "static"}),
    ],
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

