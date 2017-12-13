## SI 206 2017
## Final Project

##OBJECTIVE:
##

import requests 
import unittest
import itertools
import collections
import json
import sqlite3 
import omdb_info
import omdb
import facebook
import facebook_info 
# itunespy
#import itunes_info

##Your name: Kayla Williams

#Caching setup 

CACHE_FNAME = "FinalProject_cache.json"

try:
	cache_file = open(CACHE_FNAME,'r') # load data if you will already made cache and put into the variable
	cache_contents = cache_file.read() #file being read, not by user
	cache_file.close() #close file, it can't be read anymore 
	CACHE_DICTION = json.loads(cache_contents) #file has a string 
except:
	CACHE_DICTION = {} # creates a new variable for it 
	
### OMDB SETUP CODE: 

url = omdb_info.OMDB_ACCESS_TOKEN

def get_movie_info():
	if 'movie_info' in CACHE_DICTION:
		movie_info = CACHE_DICTION['movie_info']
		#print(len(movie_info))
	else:
		movie_info = []
		for movie in omdb_info.movie_titles:
			url = omdb_info.OMDB_ACCESS_TOKEN + movie.replace(" ", "+")
			movie_info.append(requests.get(url).json())

		CACHE_DICTION['movie_info'] = movie_info # save movie results into cache
		jsd = json.dumps(CACHE_DICTION) #save it using json 
		cache_file = open(CACHE_FNAME, 'w') #open up file 
		cache_file.write(jsd)# show file in a way that user can see it, string
		cache_file.close() #ends file, close it 
	return movie_info
movies100 = get_movie_info()

## Database consist of Movies table		

conn = sqlite3.connect('FinalProject.sqlite')
cur = conn.cursor() #connects to database 

cur.execute('DROP TABLE IF EXISTS Movies') #if table exists for users it will delete itself and make a new one 
cur.execute('CREATE TABLE IF NOT EXISTS Movies (Movie_Title TEXT, Year TEXT, Rating INTEGER, Runtime TEXT, Released TEXT)') #create database with these variables

for title in movies100:
	f = 'INSERT OR IGNORE INTO Movies VALUES (?,?,?,?,?)'
	tup = (title['Title'], title['Year'], title['Rated'], title['Runtime'], title['Released'])
	cur.execute(f, tup) # creates database for facebook 
	
conn.commit() #save the changes 

### ITUNES SET UP CODE:

# def get_from_itunes(artist,songs):

#     base_url = "http://itunes.apple.com/search" + itunes_info.replace(" ", "+")
#     params_dict = {"term":bon+iver, "entity": music}
#     resp = requests.get(base_url, params=params_dict)
#     structured_resp_text = resp.text
#     python_obj_data_from_itunes = json.loads(structured_resp_text) # the python object is a dictionary
#     itunes_dict_keys = python_obj_data_from_itunes.keys() # These keys are lists
#     for key in itunes_dict_keys:
#     		key = {TrackName}
#     		print (key) 
#     file_obj = open("itunes_file.txt", "w") #wrote a file containing a JSON formatted string and then pasted that into the JSON editor
#     file_obj.write(python_obj_data_from_itunes + "\n")
#     file_obj.close()
#     return get_from_itunes()

# def getwithCaching(baseurl, params={}):

# 	#prepped = itunes_info.jack_johnson

#     req= requests.Request(method= 'GET', url= baseurl, params= sorted(params.items()))
#     prepped = req.prepare()
#     prepped_url = prep.url 

#     #If we have made this request before, get it from CACHE_DICTION
#     if prepped_url in CACHE_DICTION:
#         return CACHE_DICTION[prepped_url]
#     else:
#         result= requests.get(baseurl, params)
#        	CACHE_DICTION[prepped_url]= result.text
#     #else (if we haven't made this request before), make actual request,
#     #add it to dictionary
# base_url= 'https://itunes.apple.com/search' #+ itunes_info.append()
# result= getwithCaching(base_url, params={'term':'Kevin Bacon'})
# print(result.url)

# ### Database consist of Albums table

# conn = sqlite3.connect('FinalProject.sqlite')
# cur = conn.cursor() #connects to database 

# cur.execute('DROP TABLE IF EXISTS Albums') #if table exists for users it will delete itself and make a new one 
# cur.execute('CREATE TABLE IF NOT EXISTS Albums (Artist TEXT, Year TEXT, Song Text, Genre TEXT)') #create database with these variables

# for name in albums100:
# 	print(name)
# 	f = 'INSERT OR IGNORE INTO Albums VALUES (?,?,?,?)'
# 	tup = (name['Artist'], name['Year'], name['Song'], name['Genre'])
# 	cur.execute(f, tup) # creates database for itunes albums
	
# conn.commit() #save the changes 

# ##Example Three
# # # Search Artist Chris Brown

# artist = itunes.search_artist('Chris Brown')[0]
# for album in artist.get_albums():
#     for track in album.get_tracks():
#         print album.get_name(), album.get_url(), track.get_name(), track.get_duration(), track.get_preview_url()

# https://itunes.apple.com/search?term=chris+brown&limit=100


#### FACEBOOK SETUP CODE:

#Authentication information in facebook_info file

access_token = facebook_info.access_token

graph = facebook.GraphAPI(access_token)
user = graph.get_object('me')
print(user)

#### END FACEBOOK SET UP CODE

#### FACEBOOK INTERACTIONS

def get_user_interactions(user):

	if user in CACHE_DICTION:
		print('cached')
		facebook_results = CACHE_DICTION[user] # grad data from cache

	else:
		print('getting data from internet')
		facebook_results = graph.get_object(id = user)

		all_fields = ['message', 'created_time', 'description', 'caption', 'link', 'place','status_type']
		all_fields = ','. join(all_fields)
		posts = graph.get_connections(id = 'me', connection_name = 'posts', fields = all_fields) 
		posts = requests.get(posts['paging']['next']).json() # atempt to make a request
		print(posts)

		CACHE_DICTION[user] = posts 
		jsd = json.dumps(CACHE_DICTION)
		cache_file = open(CACHE_FNAME, 'w')
		cache_file.close()

	return facebook_results

data = get_user_interactions(user['id'])
 





