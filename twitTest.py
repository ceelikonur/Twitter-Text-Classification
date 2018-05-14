# -*- coding: utf-8 -*-
import tweepy
import json

access_token = "560167889-WlLRCzZ6UQ1EOlJo9Gc5dbMmFmgRU1CAUoxxdnoP"
access_token_secret = "5C3GvXn8rO4rJt0IyBZShS14AqHoFgZx5Fhfecnm8PV2G"
consumer_key = "waZeDptep8tQeTU4G7N5aUWnL"
consumer_secret = "zSdiNnIJAMZtdHYzzsT90LI3aI0CWNXDCHwTxTvNRw5SE8f0Mo"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if(not api):
    print("Can not connect to the Twitter API")

data={}
istTrendCode=2344116
trTrendCode=23424969
trends = api.trends_place(id=istTrendCode)
c=0
json_data = ""
with open("testTweets2.json", "w") as t:
    for trend in trends[0]['trends']:
        print(trend['name'])
        for tweet in tweepy.Cursor(api.search,q=trend['query'],result_type="popular",language="tr").items(2):
            last = tweet.text.replace(trend['name'], "")
            dic={'id':tweet.id,'text':last,'created_at':str(tweet.created_at)}
            json.dump(data,t)




#tweets = api.user_timeline(screen_name = "yokmaalesef",count=200,exclude_replies="true",include_rts="false",max_id="962793936145338370")

#for status in tweets:
#    folC = status.user.followers_count
#    favC = status.favorite_count
 #   retC = status.retweet_count
  #  result = (favC + retC)
   # if result > 0.0:
    #    print(result," ",status._json)

#API.trends_place(id[, exclude])