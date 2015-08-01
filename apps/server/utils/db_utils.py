import settings
from bson import ObjectId

def get_mongodb_conn():
	return settings.conn 
 