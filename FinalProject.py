## SI 206 2017
## Final Project

##OBJECTIVE:
##


import unittest
import itertools
import collections
import json
import sqlite3 
import facebook

##Your name: Kayla Williams


##### FACEBOOK SETUP CODE:
# Authentication information should be in a facebook_info file...
FACEBOOK_CLIENT_ID = "1337849729677917"
FACEBOOK_CLIENT_SECRET = "5846902fff872568a63e7fe328b01f37"
FACEBOOK_GRANT_TYPE = "client_secret"

class FacebookGraphApi(object):
	"""docstring for ClassName"""
	def __init__(self, cliend_id, client_secret, grant_type):


		


		

graph = facebook.GraphAPI(access_token = "your_token", version = "2.11")

CACHE_FNAME = "FinalProject_cache.json"
# Put the rest of your caching setup here:

try:
	cache_file = open(CACHE_FNAME,'r') # load data if you will already made cache and put into the variable
	cache_contents = cache_file.read() #file being read, not by user
	cache_file.close() #close file, it can't be read anymore 
	CACHE_DICTION = json.loads(cache_contents) #file has a string 
except:
	CACHE_DICTION = {} # creates a new variable for it 

##### END FACEBOOK SET UP CODE



##### INSTAGRAM SETUP CODE:
# Authentication information should be in a instagram_info file




##### END INSTAGRAM SET UP CODE 





##### PINTEREST SETUP CODE:
# Authentication information should be in a pinterest_info file




##### END PINTEREST SETUP CODE:


#PINTEREST

#GROUPME


#GMAIL