## This gets elite proxy from https://pypi.org/project/fake-useragent/ on every request
from random import choice, shuffle

from fake_useragent import UserAgent
from pyquery import PyQuery

import urllib.request
def get_page(url):
    return urllib.request.urlopen(url).read()
#
# import urllib.request
# def get_page(url):
#     try:
#         response = urllib.request.urlopen(url)
#         html = response.read()
#         print(html)
#     except Exception as e:
#         return 'Url Error'

class Pooling(object):
	def __init__(self):
		self.proxies_url = ''

	'''returns a list of currently available elite proxies'''
	def proxy_pool(self, url = 'https://free-proxy-list.net/'):
		pq, proxies = get_page(url), []
		tr = pq('table#proxylisttable.table tbody tr')
		rows = [j.text() for j in [PyQuery(i)('td') for i in tr]]
		rows = [i for i in rows if 'elite' in i]

		for row in rows:

			row = row.split()
			data = {}
			data['ip'] = row[0]
			data['port'] = row[1]
			data['country'] = row[3]
			data['proxy'] = {
				'http' :'http://{}:{}'.format(data['ip'], data['port']),
				'https' :'https://{}:{}'.format(data['ip'], data['port'])
			}
			proxies.append(data)
		return choice(proxies)

	'''return a random list of user agents'''
	def ua_pool(self):
		ua = UserAgent()
		chromes = ua.data['browsers']['chrome'][5:40]
		shuffle(chromes)
		return choice(chromes)