import datetime
import json
import jsonpickle
import sys
import time
import wykop
from pprint import pprint

users = []

def addUser(user, count=1):
	global users
	exists = False
	for user in users:
		if not exists and author == user['author']:
			user['count'] = user['count'] + count
			exists = True
			break
	if not exists:
		users.append({
			'author': author,
			'count': count
		})

api = wykop.WykopAPI("xxx", "xxx")
#entries = api.request('tag', 'entries', ['bitcoin'], {'appkey': 'xxx', 'page': 1})
# j = json.loads(jsonpickle.encode(entries))
# pprint(j)
# sys.exit()

for page in range(1, 200):
	print datetime.datetime.now(), page
	sys.stdout.flush()
	entries = api.request('tag', 'entries', ['bitcoin'], {'appkey': 'xxx', 'page': page})
	j = json.loads(jsonpickle.encode(entries))

	# print len(j['items'])
	for item in j['items']:
		author = item['author']
		# count = item['vote_count']
		addUser(author)
		for comment in item['comments']:
			author = comment['author']
			addUser(author)

users = sorted(users, key=lambda user: user['count'], reverse=True)

with open('users.txt', 'a') as file:
	for user in users:
		file.write(user['author'] + ';' + str(user['count']) + '\n')
		# print user['author'] + ';' + str(user['count'])