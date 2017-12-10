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
#import googlemaps_geocoding 
import omdb_info
import omdb


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


##### GOOGLE MAPS GEOCODING SETUP CODE:
# def get_location(city):
# 	if city in CACHE_DICTION:
# 		print('cached')
# 		results= CACHE_DICTION[city]
# 	else:
# 		baseurl= 'https://maps.googleapis.com/maps/api/geocode/json?address='
# 		params={'key':googlemaps_geocoding.access_token_geocoding, 'outputformat': city}
# 		fullurl='baseurl'+params
# 		gresponse=json.loads(fullurl)
# 		CACHE_DICTION[city]= gresponse
# 		jsd=json.dumps(CACHE_DICTION)
# 		cache_file= open(CACHE_FNAME,'w')
# 		cache_file.write(jsd)
# 		cache_file.close()
# 	return results
# g = get_location('Pasadena,California')

## Database consist of Users table		

# conn = sqlite3.connect('FinalProject.sqlite')
# cur = conn.cursor() #connects to database 

# cur.execute('DROP TABLE IF EXISTS Users') #if table exists for users it will delete itself and make a new one 
# cur.execute('CREATE TABLE Users(post_id TEXT, post_message TEXT,post_createtime DATETIME, post_caption TEXT, post_link TEXT, post_place TEXT, post_status_type TEXT)') #create database with these variables

# for post in data:
# 	print(type(post))
# 	f = "INSERT OR IGNORE INTO Users VALUES (?,?,?,?,?)"
# 	tup =(post['id_str'], post['status_type'], post['place_Place'], post['message_string'],post['caption_string'])
# 	cur.execute(f,tup) # creates database for facebook 

# 	for use in post:
# 		u = api.get_user(use['id'])
# 		s = "INSERT OR IGNORE INTO Users Values(?,?,?,?)"
# 		tup2 = (user_id, user_message, user_createtime, user_caption, user_link, user_place, user_status_type)
# 		cur.execute(s, tup2) #creates database for table 

# conn.commit() #save the changes 

# ## query for all of the information in the Users database
# cur.execute('SELECT * FROM Users') #access the table of Users
# users_info = cur.fetchall() # get all of the information about users

### OMDB
url = omdb_info.OMDB_ACCESS_TOKEN

def get_movie_info():
	if 'movie_info' in CACHE_DICTION:
		movie_info = CACHE_DICTION['movie_info']
		print(len(movie_info))
	else:
		movie_info = []
		for movie in omdb_info.movie_titles:
			url = omdb_info.OMDB_ACCESS_TOKEN + movie.replace(" ", "+")
			movie_info.append(requests.get(url).json())

		CACHE_DICTION['movie_info'] = movie_info # save user results into cache
		jsd = json.dumps(CACHE_DICTION) #save it using json 
		cache_file = open(CACHE_FNAME, 'w') #open up file 
		cache_file.write(jsd)# show file in a way that user can see it, string
		cache_file.close() #ends file, close it 

get_movie_info()
	

