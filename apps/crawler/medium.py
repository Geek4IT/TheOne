import json
import urllib2
import traceback
from bs4 import BeautifulSoup
from pymongo import MongoClient

FEED_URL = "https://medium.com/"
FEED_SOURCE = "MEDIUM"
FEED_SOURCE_NAME = "Medium"
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB_NAME = "news"
MONGODB_COL_NAME = "feed"


def get_html_doc(url):
	resp = None
	req = urllib2.Request(url)
	req.add_header('User-Agent','fake-client')
	try:
		resp = urllib2.urlopen(req, timeout=10)
	except:
		traceback.print_exc()

	return resp

def parse_html_doc(html_doc):
	soup = BeautifulSoup(html_doc)
	group_list = soup.find('div', attrs={"class":"blockGroup blockGroup--posts js-blockGroupPosts blockGroup--inset blockGroup--list container u-size620"})
	#print group_list.prettify()
	print soup.findChildren('findChildren')
	feeds = []

	return feeds

def save_feeds(feeds):
	conn = None
	try:
		conn = MongoClient(MONGODB_HOST, int(MONGODB_PORT))
		db = conn[MONGODB_DB_NAME]
		col = db[MONGODB_COL_NAME]

		for feed in feeds:
			col.save(feed)
	except:
		traceback.print_exc()

	if conn is not None:
		conn.close()

if __name__ == "__main__":
	html_doc = get_html_doc(FEED_URL)
	feeds = parse_html_doc(html_doc)
	save_feeds(feeds)





















