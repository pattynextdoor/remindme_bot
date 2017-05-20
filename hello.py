#!/usr/bin/env python
import tweepy, time, sys, datetime
#from our keys module (keys.py), import the keys dictionary
from keys import keys

argfile = str(sys.argv[1])

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#^^ all this stuff is for authenticating

twts = api.search(q="@wyd_bot")

filename=open(argfile,'r') #opens text file
f = filename.readlines() #string named 'f' that reads all the lines of the text file
filename.close() #closes text file

#for line in f:
    #api.update_status(line) #updates status
    #time.sleep(900)#Waits 15 minutes. sleep function takes in seconds

#list of specific strings we want to check for in Tweets
t = ['@wyd_bot', '@wyd_bot to wash the dishes']



for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name #gets user's username
            m = "@%s Expect a tweet at " % (sn) #creates message 'm', customized with user's username
            s = api.update_status(m, s.id) #updates status
            time.sleep(3)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

user = api.get_user(sn)

print user.screen_name
print user.followers_count
