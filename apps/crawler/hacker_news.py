import traceback
from pymongo import MongoClient
from hn import HN, Story


FEED_URL = "https://news.ycombinator.com/"
FEED_SOURCE = "HACKER_NEWS"
FEED_SOURCE_NAME = "Hacker News"
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB_NAME = "news"
MONGODB_COL_NAME = "feed"


def save_stories(stories):
	conn = None
	try:
		conn = MongoClient(MONGODB_HOST, int(MONGODB_PORT))
		db = conn[MONGODB_DB_NAME]
		col = db[MONGODB_COL_NAME]

		print col.name

		#feeds = []
		for story in stories:
			feed = {}
			feed['name'] = story.title
			feed['tagline'] =  ""
			feed['url'] = story.link
			feed['thumbnail_url'] = ""
			feed['vote_count'] = story.points
			feed['comment_count'] = story.num_comments
			feed['source'] = FEED_SOURCE
			feed['source_name'] = FEED_SOURCE_NAME
			col.save(feed)
	echo 'Save Hacker News stories at date: '+%Y-%m-%d %H:%M:%S'' >> "/home/www/TheOne/apps/crawler.log"
	except:
		print 'error...'
		traceback.print_exc()
		echo 'Failed to save Hacker News stories at date: '+%Y-%m-%d %H:%M:%S'' >> "/home/www/TheOne/apps/crawler.log"

	if conn is not None:
		conn.close()


if __name__ == "__main__":
	hn = HN()
	stories = hn.get_stories(limit = 50)
	save_stories(stories)
	
