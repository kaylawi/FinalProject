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

# itunespy
#import itunes_info

##Your name: Kayla Williams

#Caching setup 

CACHE_FNAME = "omdb_final_project_cache.json"

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
