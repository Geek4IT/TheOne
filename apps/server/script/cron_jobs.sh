echo `Crawler at: date '+%Y-%m-%d %H:%M:%S'` >> "/home/www/TheOne/apps/crawler.log"

cd /home/www/TheOne/apps/crawler
python product_hunt.py

cd /home/www/TheOne/apps/crawler
python hacker_news.py
