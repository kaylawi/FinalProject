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
import spotipy 

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


## Database consist of Users table		

conn = sqlite3.connect('FinalProject.sqlite')
cur = conn.cursor() #connects to database 

cur.execute('DROP TABLE IF EXISTS Users') #if table exists for users it will delete itself and make a new one 
cur.execute('CREATE TABLE Users(user_id TEXT, user_likes TEXT,user_photo TEXT, user_videos TEXT)') #create database with these variables


conn.commit() #save the changes 

## query for all of the information in the Users database

cur.execute('SELECT * FROM Users') #access the table of Users
users_info = cur.fetchall() # get all of the information about users

## access exactly 100 interactions 

data = 'SELECT * FROM Users WHERE user_id LIMIT 100' # saves 100 names 
cur.execute(data) # access user names of the users from the table of Users
anything = cur.fetchall() # gets all information about names

data = 'SELECT 100 FROM Users WHERE user_likes LIMIT 100' # saves 100 likes
cur.execute(data) # access user names of the users from the table of Users
anything = cur.fetchall() # gets all information about names

data = 'SELECT 100 FROM Users WHERE user_id LIMIT 100' # saves 100 photos
cur.execute(data) # access user names of the users from the table of Users
anything = cur.fetchall() # gets all information about names

##### INSTAGRAM SETUP CODE:
# Authentication information should be in a instagram_info file

#INSTAGRAM_CLIENT_ID =
#INSTAGRAM_CLIET_SECRET = 
#INSTAGRAM_GRANT_TYPE = 
#INSTAGRAM_REDIRECT_URL = 
#CODE = 

# class InstagramApi(object):
# 	def_init_(self, client_id, client_secret, grant_type, redirect_url, code):

# 		self.client_id = client_id
# 		self.client_secret = client_secret
# 		self.grant_type = grant_type  
# 		self.redirect_url = redirect_url

# 	def access_token(self):


# access_token_url = 'https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code'


##### END INSTAGRAM SET UP CODE 





##### PINTEREST SETUP CODE:
##Authentication information should be in a pinterest_info file

# PINTEREST_CLIENT_ID = "4937510988336347780"
# PINTEREST_CLIENT_SECRET = "19b9ff970a6789efae1a0933ec5f07cb9077c9886492f528b2c8b9eb45496db3"
# PINTEREST_GRANT_TYPE = "client_credentials"

#function give us access to creating a token 

# class PinterestApi(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, client_id, client_secret, grant_type):

# 		self.client_id = client_id
# 		self.client_secret = client_secret
# 		self.grant_type = grant_type  

# #have access to client id, client secret, grant type because these variables are in the class "self"

# 	def access_token(self):

# 		access_token_url = "https://api.pinterest.com/oauth/access_token?" #request will always know to look for a url 

# 		#can only access dictuionary for api

# 		param = {"client_id" : self.client_id, "client_secret" : self.client_secret ,"grant_type" : self.grant_type} #have to use key word params because it will recognize it 

# 		r = requests.get(access_token_url,params = param) 

# 		return r.json()['access_token']

# test = PinterestApi(PINTEREST_CLIENT_ID, PINTEREST_CLIENT_SECRET, PINTEREST_GRANT_TYPE)

# pinterstaccesstoken = test.access_token()

# print(pinterestaccesstoken)


#### END PINTEREST SETUP CODE:

#### PINTEREST INTERACTIONS 

# get_user_interaction 

# def get_pinterest_user_interactions(user):

# 	if user in CACHE_DICTION:
# 		print('cached')
# 		facebook_results = CACHE_DICTION[user] # grab data from cache

# 	else:
# 		print('getting data from internet') 
# 		user = graph.get_object(id = user_id)
# 		print (user['likes'])

# 		print(facebook_results)

# 		CACHE_DICTION[user] = facebook_results # save facebook results into cache
# 		sd = json.dumps(CACHE_DICTION) #save it using json 
# 		cache_file = open(CACHE_FNAME, 'w') #open up file 
# 		cache_file.write(jsd)# show file in a way that user can see it, string
# 		cache_file.close() #ends file, close it 


# 		return pinterest_results

		



#DROPBOX


#SPOTIFY



##### SPOTIFY SETUP CODE:

# token = util.prompt_for_user_token('Kayla Williams','user-top-read')

# export SPOTIPY_CLIENT_ID = 'e4a316bf49ac46ccbbf03d2fc27a89c1'
# export SPOTIPY_CLIENT_SECRET = '9db5f1f2cc4e473caeeb7a283bf6dc64'
#export SPOTIPY_REDIRECT_URI ='your-app-redirect-url'



##### END SPOTIFY SETUP CODE:

