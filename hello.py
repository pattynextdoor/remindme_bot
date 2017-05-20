#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'Lj2w4F4vzXZ653dSNkqzqmn10'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'WLGT1JUNJ3aNaHacS9deM9iYcj0w3NDJodVHKbaMpXbdACOHxA'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '865969434170597376-dcKEGVfVlQnaZryFFglcrIE6RxNphba'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'KLFeCkjJVABDEywnM7z74cXsD401vlsmNm9pma9Aty11B'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r') #opens text file
f=filename.readlines() #string named 'f' that reads all the lines of the text file
filename.close() #closes text file

for line in f:
    api.update_status(line) #updates status
    time.sleep(900)#Waits 15 minutes. sleep function takes in seconds
