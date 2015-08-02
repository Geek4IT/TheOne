import os
import tornado.template
from pymongo import MongoClient
from tornado.options import define, options

DEBUG = True

path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

TEMPLATE_ROOT = path(ROOT, 'templates')
MEDIA_ROOT = path(ROOT, 'media')

PROJECT_SETTING = {
	"cookie_secret": "JDJCNKNkckKSJCNKNjskcqwiozqacsjkSWDIOknSJkkkn=",
        "login_url": "/login"
}

SSL_OPTIONS = None  

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017

conn = MongoClient(MONGODB_HOST, MONGODB_PORT)

settings = {}
settings['debug'] = True
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "6e2a661f-e2ea-43c3-a0a8-a1a679324dca"
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)

SYSLOG_TAG = "TheOne"

if options.config:
	tornado.options.parse_config_file(options.config)
