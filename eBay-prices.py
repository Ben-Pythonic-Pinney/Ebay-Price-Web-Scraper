# eBay-Price-Web-Scraper
# Created By: Ben Pinney
# Example: python[version] scrape.py [item]

from bs4 import BeautifulSoup
import requests
import sys

item = sys.argv[1]

r = requests.get('https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0&_ipg=9999'.format(item))

command = BeautifulSoup(r.content, 'html.parser')

result = command.find_all('div', {'class':'s-item__details clearfix'})

for price in result:
	try:
		print(price.find('span', {'class':'ITALIC'}).text.strip())

	except:
		print(price.find('span', {'class':'s-item__price'}).text.strip())
		continue