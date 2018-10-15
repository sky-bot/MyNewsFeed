import feedparser
from flask import Flask
from flask import render_template
from flask import request
import datetime
now = datetime.datetime.now()

app = Flask(__name__)

Toi = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms" 
Mint = "http://www.livemint.com/rss/homepage"
Hin = "https://www.thehindu.com/feeder/default.rss"
Ndtv = "http://feeds.feedburner.com/ndtvnews-india-news"
Economic_times = "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
IndianExpress = "https://indianexpress.com/section/india/feed/"
CNBC = "https://www.cnbc.com/id/100003114/device/rss/rss.html"

@app.route("/")
def get_news():
	feed = feedparser.parse(Toi)
	feed1 = feedparser.parse(Mint)
	feed2 = feedparser.parse(Hin)
	feed3 = feedparser.parse(Ndtv)
	feed4 = feedparser.parse(Economic_times)
	feed5 = feedparser.parse(IndianExpress)
	

	for news in feed1['entries']: 
		start = news.summary.find('<')
		last = news.summary.find('>')

		news.summary=news.summary[last+1:]
		
		

	return render_template("home.html",articles = feed['entries'][:5],articles1=feed1['entries'][:5],articles2=feed2['entries'][:10],
		articles3=feed3['entries'][:9],articles4=feed4['entries'][:7],articles5=feed5['entries'][:15],now=now.strftime("%d, %b %Y | %H:%M"))

	

if __name__=="__main__":
	app.run(port=5000,debug=True)