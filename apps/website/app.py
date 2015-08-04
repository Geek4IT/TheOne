import os
import sys

import tornado.httpserver
import tornado.ioloop
from tornado.options import options
import tornado.web

from settings import settings
from urls import url_patterns

class App(tornado.web.Application):
	def __init__(self):
		tornado.web.Application.__init__(self, url_patterns, **settings)

def main():
	app = App()
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
