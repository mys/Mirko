import datetime
import json
import jsonpickle
import sys
import time
import wykop
from pprint import pprint

api = wykop.WykopAPI('aNd401dAPp', '3lWf1lCxD6')
result = api.authenticate(login='satoshi', password='')

for page in range(1, 2):
#	print page
	entries = api.request('tag', 'entries', ['bitcoin'], {'appkey': 'aNd401dAPp', 'page': page})
	j = json.loads(jsonpickle.encode(entries))
	for item in j['items']:
#		print item['date']
		vote = True
		for author in item['voters']:
			if author['author'] == 'satoshi':
				vote = False
		if vote:
#			print 'vote+'
			result = api.vote_entry(item['id'])
#			sys.exit()
