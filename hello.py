#!/usr/bin/env python
import tweepy, time, sys, datetime, string
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
    #tweet_count_before = api.get_user(sn).statuses_count
    m = "@%(sn)s Okay %(sname)s, I'll remind you %(task)s." % {'sn': sn, 'sname': sname, 'task': task}#creates message 'm', customized with user's username
    s = api.update_status(m, s.id) #updates status
    time.sleep(3) #arbitrary time

    timeString = task.rfind(" in ")
    taskWithout = task[0:timeString]
    print taskWithout
    timeSet = task[timeString+4:]
    print timeSet
    timeMagnitude = timeSet[0:1]
    print timeMagnitude
    timeUnits = timeSet[2:]
    print timeUnits

    timeMagnitudeInt = int(timeMagnitude)
    print timeMagnitudeInt

    if timeUnits == "hours" or timeUnits == "hour":
        time.sleep(timeMagnitudeInt * 3600)
    if timeUnits == "minutes" or timeUnits == "minute":
        time.sleep(timeMagnitudeInt * 60)


    for s in twts:
        sn = s.user.screen_name #gets user's username
        sname = s.user.name
        m = "@%(sn)s Okay %(sname)s, it's time %(taskWithout)s" % {'sn': sn, 'sname': sname, 'taskWithout' : taskWithout}#creates message 'm', customized with user's username
        s = api.update_status(m, s.id) #updates status
        time.sleep(3) #arbitrary time



    #tweet_before = api.user_timeline(id=sn, count=1)
    #for tweet in public_tweets: #prints all tweets that bot has
    #    print tweet.text

    #user = api.get_user(sn)

    #print user.screen_name
    #print user.followers_count
    #time.sleep(30)
