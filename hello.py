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

while True:
    twts = api.search(q="@remindme_bot")

    for s in twts:
        if not s.favorited:
            sn = s.user.screen_name #gets user's username
            sname = s.user.name
            task = s.text[14:]
            print "Bot on task of \"%(task)s\" from user named @%(sn)s" % {'task' : task, 'sn' : sn}
            #tweet_count_before = api.get_user(sn).statuses_count
            m = "@%(sn)s Okay %(sname)s, I'll remind you %(task)s." % {'sn': sn, 'sname': sname, 'task': task}#creates message 'm', customized with user's username
            try:
                api.update_status(m, s.id) #updates status
            except tweepy.error.TweepError:
                continue
            time.sleep(1) #arbitrary time

            timeString = task.rfind(" in ")
            taskWithout = task[0:timeString]

            timeSet = task[timeString+4:]

            timeMagnitude = timeSet[0:2]
            if(timeMagnitude[1] == ' '):
                timeMagnitude = timeSet[0:1]
            print timeMagnitude
            timeUnits = timeSet[2:]
            print timeUnits

            timeMagnitudeInt = int(timeMagnitude)
            timeMagDec = timeMagnitudeInt

            print "Counting down..."

            if timeUnits == "days" or timeUnits == "day":
                time.sleep(timeMagnitudeInt * 3600 * 60)
            if timeUnits == "hours" or timeUnits == "hour":
                time.sleep(timeMagnitudeInt * 3600)
            if timeUnits == "minutes" or timeUnits == "minute":
                time.sleep(timeMagnitudeInt * 60)
            else:
                time.sleep(timeMagnitudeInt)

            m = "@%(sn)s Okay %(sname)s, it's time %(taskWithout)s" % {'sn': sn, 'sname': sname, 'taskWithout' : taskWithout}#creates message 'm', customized with user's username
            try:
                api.update_status(m, s.id) #updates status
            except tweepy.error.TweepError:
                pass
            try:
                api.create_favorite(s.id)
            except tweepy.error.TweepError:
                pass
