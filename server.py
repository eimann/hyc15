#!/usr/bin/env python

import os.path
import logging
import uuid
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.escape
import tornado.web

from tornado.escape import json_encode
from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)


# The MainHandler returns the index.html to the client

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

# The IdHandler generates a specific UUID for the client to track its state
# TODO: the UUID should be saved in Redis to persist state for the client during the game and for 30 minutes after the game ended

class IdHandler(tornado.web.RequestHandler):
    def get(self):
        clientid = { 'id': str(uuid.uuid4()) }
        self.set_header('Content-Type', 'application/javascript')
        self.write(json_encode(clientid))

# The ColorHandler receives the color value selected by the client and saves it with the client Id in the Redis database

class ColorHandler(tornado.web.RequestHandler):
    def post(self):
        print(self.request.body)
        data_json = tornado.escape.json_decode(self.request.body)
        # TODO: parsing works, Redis code goes here

def main():
    tornado.options.parse_command_line()
    # Define request routes to be available to the client
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

