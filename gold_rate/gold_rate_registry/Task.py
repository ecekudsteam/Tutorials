from flask_restful import Resource
import requests

class Task(Resource):
	
	def get(self):
		headers = {
    		'Accept-Encoding': 'gzip, deflate, sdch',
    		'Accept-Language': 'en-US,en;q=0.8',
    		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    		'Referer': 'http://www.wikipedia.org/',
    		'Connection': 'keep-alive',
			}
		url = "https://data-asg.goldprice.org/dbXRates/USD"
		r = requests.get(url=url,headers=headers)
		data = r.json()

		g_rate = data["items"][0]["xauPrice"]
		return "Current gold price is {} USD".format(g_rate)

		