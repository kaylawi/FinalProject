
import requests 
import unittest
import itertools
import collections
import json
import sqlite3 
import facebook
import facebook_info

##Your name: Kayla Williams

#Caching setup 

CACHE_FNAME = "facebook_final_project_cache.json"

try:
	cache_file = open(CACHE_FNAME,'r') # load data if you will already made cache and put into the variable
	cache_contents = cache_file.read() #file being read, not by user
	cache_file.close() #close file, it can't be read anymore 
	CACHE_DICTION = json.loads(cache_contents) #file has a string 
except:
	CACHE_DICTION = {} # creates a new variable for it 

#### FACEBOOK SETUP CODE:

#Authentication information in facebook_info file

access_token = facebook_info.access_token

graph = facebook.GraphAPI(access_token)
user = graph.get_object('me')

#### END FACEBOOK SET UP CODE

#### FACEBOOK INTERACTIONS

def get_user_interactions(user):

	if user in CACHE_DICTION:
		print('cached')
		facebook_results = CACHE_DICTION[user] # grad data from cache

	else:
		facebook_results = graph.get_object(id = user)

		all_fields = ['created_time', 'description', 'caption', 'link', 'place','status_type']
		all_fields = ','. join(all_fields)
		posts = graph.get_connections(id = 'me', connection_name = 'posts', fields = all_fields) 
		posts = requests.get(posts['paging']['next']).json() # atempt to make a request
		
		CACHE_DICTION[user] = posts 
		jsd = json.dumps(CACHE_DICTION)
		cache_file = open(CACHE_FNAME, 'w')
		cache_file.write(jsd)# show file in a way that user can see it, string
		cache_file.close()

	return CACHE_DICTION[user]

posts100 = get_user_interactions('10202862168937730')

## Database consist of Movies table		

conn = sqlite3.connect('FinalProject.sqlite')
cur = conn.cursor() #connects to database 

cur.execute('DROP TABLE IF EXISTS Posts') #if table exists for users it will delete itself and make a new one 
cur.execute('CREATE TABLE IF NOT EXISTS Posts (created_time TEXT, link TEXT, status_type TEXT)') #create database with these variables

for post in posts100['data']:
	p = 'INSERT OR IGNORE INTO Posts VALUES (?,?,?)'
	tup = (post['created_time'], post['link'], post['status_type'])
	cur.execute(p, tup) # creates database for facebook 

conn.commit() # save the changes 
