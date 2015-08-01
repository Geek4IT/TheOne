import json
import urllib2
import traceback
from bs4 import BeautifulSoup
from pymongo import MongoClient

FEED_URL = "http://www.producthunt.com"
FEED_SOURCE = "PRODUCT_HUNT"
FEED_SOURCE_NAME = "Product Hunt"
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB_NAME = "news"
MONGODB_COL_NAME = "feed"

def get_html_doc(url):
	resp = None
	req = urllib2.Request(url)
	req.add_header('User-Agent','fake-client')
	try:
		resp = urllib2.urlopen(req, timeout=15)
	except:
		traceback.print_exc()
	return resp.read()


def parse_html_doc(html_doc):
	soup = BeautifulSoup(html_doc, "html.parser")
	attrs={"data-react-class":"FeaturedFeed"}
	content = soup.findAll("div",attrs)
	parsedStr = content[0].get('data-react-props')
	parsedJson = json.loads(parsedStr)
	post_groups = parsedJson.get('post_groups')

	feeds = []

	for postsDic in post_groups:
		postsDic = postsDic.get('posts')
		for postDic in postsDic:
			feed = {}
			feed['name'] = postDic['name']
			feed['tagline'] =  postDic['tagline']
			feed['url'] = FEED_URL + postDic['url']
			feed['thumbnail_url'] = postDic['thumbnail_url']
			feed['vote_count'] = postDic['vote_count']
			feed['comment_count'] = postDic['comment_count']
			feed['source'] = FEED_SOURCE
			feed['source_name'] = FEED_SOURCE_NAME

			feeds.append(feed)
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
	html_doc= get_html_doc(FEED_URL)
	feeds = parse_html_doc(html_doc)
	save_feeds(feeds)
