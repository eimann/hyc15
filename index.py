#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the RevealYourCity backend service. Nothing to see here.")

class IdHandler(tornado.web.RequestHandler):
    def get(self):
        message = {
            "id": str(uuid.uuid4()),
        } 

class ColorHandler(tornado.web.RequestHandler):
    def post(self):
        message = {
            "id": str(uuid.uuid4()),
            "color": self.get_argument("color"),
        }
        # to_basestring is necessary for Python 3's json encoder,
        # which doesn't accept byte strings.
        message = tornado.escape.to_basestring(
        self.write(color)
        global_message_buffer.new_messages([message]))

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/GetId", IdHandler),
        (r"/SetColor", ColorHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

