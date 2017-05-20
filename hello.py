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


twts = api.search(q="@remindme_bot")

tweet_count_before = 0

for s in twts:
    sn = s.user.screen_name #gets user's username
    sname = s.user.name
    task = s.text[14:]
    print task
    tweet_count_before = api.get_user(sn).statuses_count
    m = "@%(sn)s Okay %(sname)s, I'll remind you %(task)s." % {'sn': sn, 'sname': sname, 'task': task}#creates message 'm', customized with user's username
    s = api.update_status(m, s.id) #updates status
    time.sleep(3) #arbitrary time

    while(tweet_count_before <= api.get_user(sn).statuses_count):
        print "searching for new tweets..."
        time.sleep(2)
        if (tweet_count_before < api.get_user(sn).statuses_count):
            print "done"
            break

    for s in twts:
        sn = s.user.screen_name #gets user's username
        sname = s.user.name
        m = "@%(sn)s Okay %(sname)s, it's time." % {'sn': sn, 'sname': sname}#creates message 'm', customized with user's username
        s = api.update_status(m, s.id) #updates status
        time.sleep(3) #arbitrary time

for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
    except:
        pass





    #tweet_before = api.user_timeline(id=sn, count=1)
    #for tweet in public_tweets: #prints all tweets that bot has
    #    print tweet.text

    #user = api.get_user(sn)

    #print user.screen_name
    #print user.followers_count
    #time.sleep(30)
