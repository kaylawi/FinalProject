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
import facebook

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

##### FACEBOOK SETUP CODE:
# Authentication information should be in a facebook_info file...

#get access to access token 
#have to create token because it is temporary and want access to it forever, therefore request is helpful as it gives information whenever we want it

FACEBOOK_CLIENT_ID = "1337849729677917"
FACEBOOK_CLIENT_SECRET = "5846902fff872568a63e7fe328b01f37"
FACEBOOK_GRANT_TYPE = "client_credentials"

#function give us access to creating a token 

class FacebookGraphApi(object):
	"""docstring for ClassName"""
	def __init__(self, client_id, client_secret, grant_type):

		self.client_id = client_id
		self.client_secret = client_secret
		self.grant_type = grant_type  

#have access to client id, client secret, grant type because these variables are in the class "self"
	def access_token(self):

		access_token_url = "https://graph.facebook.com/oauth/access_token?" #request will always know to look for a url 

		#can only access dictuionary for api

		param = {"client_id" : self.client_id, "client_secret" : self.client_secret ,"grant_type" : self.grant_type} #have to use key word params because it will recognize it 

		r = requests.get(access_token_url,params = param) 

		return r.json()['access_token']

test = FacebookGraphApi(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, FACEBOOK_GRANT_TYPE)

facebookaccesstoken = test.access_token()

print(facebookaccesstoken)


graph = facebook.GraphAPI(access_token = facebookaccesstoken, version = "2.11")

##### END FACEBOOK SET UP CODE

##### FACEBOOK INTERACTIONS 

# get_user_interaction 

def get_user_interactions(user):

	if user in CACHE_DICTION:
		print('cached')
		facebook_results = CACHE_DICTION[user] # grab data from cache

	else:
		print('getting data from internet') 
		user = graph.get_object(id = user_id)
		print (user['likes'])

		print(facebook_results)

		CACHE_DICTION[user] = facebook_results # save facebook results into cache
		sd = json.dumps(CACHE_DICTION) #save it using json 
		cache_file = open(CACHE_FNAME, 'w') #open up file 
		cache_file.write(jsd)# show file in a way that user can see it, string
		cache_file.close() #ends file, close it 


		return facebook_results

# facebook_interactions =
# facebook_daysofinteractions =





##### INSTAGRAM SETUP CODE:
# Authentication information should be in a instagram_info file






##### END INSTAGRAM SET UP CODE 





##### PINTEREST SETUP CODE:
# Authentication information should be in a pinterest_info file




##### END PINTEREST SETUP CODE:


#PINTEREST

#GROUPME


#GMAIL