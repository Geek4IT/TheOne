import gzip
import json
import StringIO
import pymongo
from utils.db_utils import get_mongodb_conn
from settings import conn 
from bson import ObjectId
from tornado.web import RequestHandler, asynchronous

class JSONEncoder(json.JSONEncoder):
	def default(self,obj):
		if isinstance(obj, ObjectId):
			return str(obj)
		return json.JSONEncoder.default(self,obj)

def zip_content(content):
    buf = StringIO.StringIO()
    content = JSONEncoder().encode(content)
    # content = json.dumps(content)
    fp = gzip.GzipFile(mode='wb', compresslevel=9, fileobj=buf)
    fp.write(str(content))
    fp.close()
    return buf.getvalue()

def finish_request(request, content, compress=False):
    request.set_header("Content-Type", 'application/Json; charset="utf-8"')
    if compress:
        request.set_header('Content-Encoding', 'gzip')
        request.write(zip_content(content))
    else:
        request.write(content)
    request.finish()

class FeedsHandler(RequestHandler):
	@asynchronous
	def get(self):
		source = self.get_argument("source", None)

		conn = get_mongodb_conn()
		db = conn.news
		table = db.feed
		feedsVal = None
		if source:
			feedsVal = table.find({"source":source})
		else:
			feedsVal = table.find()

		print feedsVal.count()
		feeds = list(feedsVal)

		finish_request(self,feeds,True)

class FeedHandler(RequestHandler):
	@asynchronous
	def get(self):
		
		conn = get_mongodb_conn()
		db = conn.news
		table = db.feed
		feedsVal = table.find()
		print feedsVal.count()
		feeds = list(feedsVal)

		finish_request(self,feeds,True)










