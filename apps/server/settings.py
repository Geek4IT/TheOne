import os
from pymongo import Connection

DEBUG = True
_this_dir = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(_this_dir, 'templates')
STATIC_DIR = os.path.join(_this_dir, 'static')

PROJECT_SETTING = {
	"cookie_secret": "JDJCNKNkckKSJCNKNjskcqwiozqacsjkSWDIOknSJkkkn=",
    "login_url": "/login"
}

SSL_OPTIONS = None  

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017

conn = Connection(host=MONGODB_HOST, port=MONGODB_PORT)