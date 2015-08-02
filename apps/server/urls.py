from handlers.feed import *

url_patterns = [	
	(r'/',IndexHandler),
	(r'/feeds', FeedsHandler),
	(r'/feed', FeedHandler),
]
