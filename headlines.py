import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
import urllib2
import urllib
import datetime
now = datetime.datetime.now()

app = Flask(__name__)

Hin = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml" 
Mint = "http://www.livemint.com/rss/homepage"
Toi = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

@app.route("/")
def get_news():
	feed = feedparser.parse(Hin)
	feed1 = feedparser.parse(Mint)
	feed2 = feedparser.parse(Toi)
	#weather = get_weather("London,UK")

	for news in feed1['entries']: 
		start = news.summary.find('<')
		last = news.summary.find('>')
		print news.summary
		print str(start)+" "+str(last)
		news.summary=news.summary[last+1:]
		print news.summary[:last]
		print "-------------"

	return render_template("home.html",articles = feed['entries'][:5],articles1=feed1['entries'][:5],articles2=feed2['entries'][:5],
	now=now.strftime("%d, %b %Y | %H:%M"))

# def get_weather(query):

# 	api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f728444e3909d51ad36cf51b03c11d01"

# 	query = urllib.quote(query)
# 	url = api_url.format(query)
# 	print url
# 	data = urllib2.urlopen(url).read()
# 	parsed = json.loads(data)
# 	weather = None
# 	if parsed.get("weather"):
# 		weather={"description":parsed["weather"][0]["description"],"temperature":parsed["main"]["temp"],"city":parsed["name"]}

# 	return weather	

if __name__=="__main__":
	app.run(port=5000,debug=True)