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
# import facebook
# import facebook_info 
import itunespy

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
movies100 =get_movie_info()


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

def get_album_info():
	if 'album_info' in CACHE_DICTION:
		album_info = CACHE_DICTION['album_info']
		print(len(album_info))

	else:
		album_info = []
		artist = itunespy.search_artist('Johnny Cash') # returns a list
		albums = artist[0].get_albums() # get songs 
		for a in range(len(albums)):
			print(albums[a])
			album_info.append(albums[a])

# 		CACHE_DICTION['album_info'] = album_info # save album results into cache
# 		jsd = json.dumps(CACHE_DICTION) #save it using json 
# 		cache_file = open(CACHE_FNAME, 'w') #open up file 
# 		cache_file.write(jsd)# show file in a way that user can see it, string
# 		cache_file.close() #ends file, close it 
# 	return album_info
albums100 =get_album_info()

['collection_name'][]


### Database consist of Albums table

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


# ### Example One
def get_from_itunes(artist,songs):

    base_url = "http://itunes.apple.com/search"
    params_dict = {"term":bon+iver, "entity": music}
    resp = requests.get(base_url, params=params_dict)
    Jack_Johnson_Music = Jack_Johnson_Music.text
    Music_from_itunes = json.loads(Jack_Johnson_Music)
    structured_resp_text = resp.text
    python_obj_data_from_itunes = json.loads(structured_resp_text)
# the python object is a dictionary
    itunes_dict_keys = python_obj_data_from_itunes.keys() # These keys are lists
    for key in itunes_dict_keys:

        print (key) # it's unicode. I have no clue how to proceed from here.
# I should be getting a dictionary
# And then getting to the key Track Name

#     file_obj = open("CACHE_FNAME", "w") 
#     file_obj.write(python_obj_data_from_itunes + "\n")
#     file_obj.close()

#     return get_from_itunes()

# ### Example Two 

#     class Song():
# def __init__(self, song_dict={}):
#     self.trackName = song_dict["trackName"]
#     self.trackNumber = song_dict["trackNumber"]
#     self.primaryGenreName = song_dict["primaryGenreName"]


# ##Example Three
# # # Search Artist Chris Brown

# artist = itunes.search_artist('Chris Brown')[0]
# for album in artist.get_albums():
#     for track in album.get_tracks():
#         print album.get_name(), album.get_url(), track.get_name(), track.get_duration(), track.get_preview_url()

# https://itunes.apple.com/search?term=chris+brown&limit=100

### FACEBOOK SET UP CODE:

 ##Authentication information should be in a facebook_info file...
  
# facebookaccesstoken = test.access_token()
# access_token = facebook_info.FACEBOOK_access_token
  
#  print(facebookaccesstoken)
# graph = facebook.GraphAPI(access_token)
# user = graph.get_object('me') 
# print(user)
  
  
# graph = facebook.GraphAPI(access_token = facebookaccesstoken, version = "2.11")
  
#  ##### END FACEBOOK SET UP CODE
  
#  ##### FACEBOOK INTERACTIONS 
  
# def get_user_interactions(user):

#   	if user in CACHE_DICTION:
#   		print('cached')
#   		facebook_results = CACHE_DICTION[user] # grab data from cache
  
#  	for user in users['data']:

#  	data = graph.request('/v2.2/search?type=event&q=&since=2016-01-01&limit=1000')

#  		 	return data 

 
  	# else:
 #  		print('getting data from internet') 
 # 		user = graph.get_object(id = user_id,count = 100)
 # 		print (user['likes'])
 # 		facebook_results = graph.get_object(id = user)
 		
 # 		all_fields = ['message', 'created_time', 'description', 'caption', 'link', 'place', 'status_type']
 # 		all_fields = ','.join(all_fields)
 # 		posts = graph.get_connections(id = 'me', connection_name = 'posts', fields = all_fields) # + posts['paging']['cursors']['after'])
 # 		posts = requests.get(posts['paging']['next']).json() #attempt to make a request to next page of data,if exists
 # 		print(posts) 
  
 # 		print(facebook_results)
  
 # 		CACHE_DICTION[user] = facebook_results # save facebook results into cache
 # 		sd = json.dumps(CACHE_DICTION) #save it using json 
 # 		CACHE_DICTION[user] = posts # save user results into cache
 # 		jsd = json.dumps(CACHE_DICTION) #save it using json 
 #  		cache_file = open(CACHE_FNAME, 'w') #open up file 
 #  		cache_file.write(jsd)# show file in a way that user can see it, string
 #  		cache_file.close() #ends file, close it 
  
  
 # 		return facebook_results
 
 
 # data = get_user_interactions('Kayla Williams')
 
 ## Database consist of Users table		
 
 # conn = sqlite3.connect('FinalProject.sqlite')
 # cur = conn.cursor() #connects to database 
 
 #  cur.execute('DROP TABLE IF EXISTS Users') #if table exists for users it will delete itself and make a new one 
 #  cur.execute('CREATE TABLE Users(user_id TEXT, user_likes INTEGER,user_photo TEXT)') #create database with these variables
 
 
 #  conn.commit() #save the changes 
 
 # ## query for all of the information in the Users database
 
 #  cur.execute('SELECT * FROM Users') #access the table of Users
 #  users_info = cur.fetchall() # get all of the information about users





