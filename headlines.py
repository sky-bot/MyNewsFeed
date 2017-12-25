import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
import urllib2
import urllib
import re


app = Flask(__name__)

RSS_FEED = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
			'cnn':'http://rss.cnn.com/rss/edition_world.rss',
			'mint':'http://www.livemint.com/rss/homepage'}

@app.route("/",methods=['GET','POST'])
def get_news():
	query = request.form.get("publication")

	if not query or query.lower() not in RSS_FEED:
		publication="mint"
	else:
		publication = query.lower()

	feed = feedparser.parse(RSS_FEED[publication])

	result=[]
	summ=[]
	for article in feed['entries']:
		print article.title
		find=re.match(r'<',article.summary)
		find1=re.match(r'>',article.summary)
		
		if find==None or find1==None:
			continue

		start=find.start()
		print start
		print "ashish"

		end=find1.end()
		
		result.add(article.summary[start:end+1])
		articles.add(article.summary[end+1:])
		print result
	  

	weather = get_weather("London,UK")
	return render_template("home.html",articles = feed['entries'],weather=weather)

def get_weather(query):

	api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f728444e3909d51ad36cf51b03c11d01"

	query = urllib.quote(query)
	url = api_url.format(query)
	print url
	data = urllib2.urlopen(url).read()
	parsed = json.loads(data)
	weather = None
	if parsed.get("weather"):
		weather={"description":parsed["weather"][0]["description"],"temperature":parsed["main"]["temp"],"city":parsed["name"]}

	return weather	

if __name__ == "__main__":
	app.run(port =5000, debug =True)