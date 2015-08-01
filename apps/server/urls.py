from views.api_views import *

APIS = [	
	(r'/feeds', FeedsHandler),
	(r'/feed', FeedHandler),
]