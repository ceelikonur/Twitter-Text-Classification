import io
import json
import re
import tweepy
def clear(text):
    r1 = re.sub("#\S+|@\S+|http\S+|[^a-zA-Z ĞÜŞİÖÇğüşıöç]", "", text)
    r2 = re.sub("[ \t]{2,}|\t|\n"," ", r1)
    return r2.lower()


def percent(fav,ret):
    ss = (ret*10+fav)/100
    ss = round(ss, 4)
    if ss > 100:
        ss = 100
    return ss


access_token = "560167889-WlLRCzZ6UQ1EOlJo9Gc5dbMmFmgRU1CAUoxxdnoP"
access_token_secret = "5C3GvXn8rO4rJt0IyBZShS14AqHoFgZx5Fhfecnm8PV2G"
consumer_key = "waZeDptep8tQeTU4G7N5aUWnL"
consumer_secret = "zSdiNnIJAMZtdHYzzsT90LI3aI0CWNXDCHwTxTvNRw5SE8f0Mo"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if not api:
    print("Can not connect to the Twitter API")

acc = ['MaisonValentino', 'CHANEL', 'Prada', 'gucci', 'Coach', 'TommyHilfiger', 'UnderArmour', 'nike', 'VANS_66', 'PUMA', 'LEVIS', 'LACOSTE', 'Converse', 'CalvinKlein','adidas']
tweets = []
i=0
for a in acc:
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=a, tweet_mode="extended", count="200",
                               exclude_replies="true", include_rts="false").items():
        pop = percent(tweet.favorite_count, tweet.retweet_count)
        if pop > 1:
            text = clear(tweet.full_text)
            tweets.append({'id': tweet.id, 'text': text, 'score': pop, 'company': a})
            i += 1
            print(i,a,pop,text)

#with open("mainData.json", 'w', encoding='utf8') as t:
    #json.dump(tweets, t, ensure_ascii=False)