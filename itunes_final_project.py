import requests 
import unittest
import itertools
import collections
import json
import sqlite3 
import itunes_info

## ITUNES SET UP CODE:


#Caching setup 

CACHE_FNAME = "FinalProject_cache.json"

try:
	cache_file = open(CACHE_FNAME,'r') # load data if you will already made cache and put into the variable
	cache_contents = cache_file.read() #file being read, not by user
	cache_file.close() #close file, it can't be read anymore 
	CACHE_DICTION = json.loads(cache_contents) #file has a string 
except:
	CACHE_DICTION = {} # creates a new variable for it 

def getwithCaching():
    #If we have made this request before, get it from CACHE_DICTION
    if 'itunes' in CACHE_DICTION:
    	return CACHE_DICTION['itunes']
    else:
    	chris_brown = requests.get(itunes_info.chris_brown).json()
    	beyonce = requests.get(itunes_info.beyonce).json()
    	jack_johnson = requests.get(itunes_info.jack_johnson).json()
    	results = [chris_brown, beyonce, jack_johnson]
    	CACHE_DICTION['itunes'] = results
    	jsd = json.dumps(CACHE_DICTION)
    	cache_file = open(CACHE_FNAME, 'w')
    	cache_file.write(jsd)# show file in a way that user can see it, string
    	cache_file.close()
    # else (if we haven't made this request before), make actual request,
    # add it to dictionary
    return CACHE_DICTION['itunes']
result = getwithCaching()

### Database consist of Albums table

conn = sqlite3.connect('FinalProject.sqlite')
cur = conn.cursor() #connects to database 

cur.execute('DROP TABLE IF EXISTS Albums') #if table exists for users it will delete itself and make a new one 
cur.execute('CREATE TABLE IF NOT EXISTS Albums (Track TEXT, Artist TEXT, Year TEXT, Song Text, Genre TEXT)') #create database with these variables

for i in range(len(result)):
	for n in range(len(result[i]['results'])):
		f = 'INSERT OR IGNORE INTO Albums VALUES (?,?,?,?,?)'
		tup = (result[i]['results'][n]['trackName'], result[i]['results'][n]['artistName'], result[i]['results'][n]['releaseDate'], result[i]['results'][n]['trackName'], result[i]['results'][n]['primaryGenreName'])
		cur.execute(f, tup) # creates database for itunes albums
	
conn.commit() #save the changes 