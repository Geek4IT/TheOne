import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from settings import DEBUG, TEMPLATE_DIR, STATIC_DIR, PROJECT_SETTING, SSL_OPTIONS
from urls import APIS

define('port',default=9999,help='Run on the given poer', type=int)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=APIS,
								  template_path=TEMPLATE_DIR,
								  static_path=STATIC_DIR,
								  debug=DEBUG,
								  **PROJECT_SETTING)
	http_server = tornado.httpserver.HTTPServer(app,ssl_options=SSL_OPTIONS,xheaders=True)
	http_server.listen(options.port)
	print "Start tornado server, listening port:%s" % options.port
	tornado.ioloop.IOLoop.instance().start()
