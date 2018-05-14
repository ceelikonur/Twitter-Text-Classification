import json
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tweepy

with open("dictionary.json", encoding='utf8') as jsonFile:
    dic = json.load(jsonFile)
dic = pd.DataFrame(dic)

with open("classifiedData.json", encoding='utf8') as jsonFile:
    data = json.load(jsonFile)
data = pd.DataFrame(data)


x = dic[dic['class'] == '4'].groupby('word').count()
print(x.sort_values(by='class', ascending=False).head(60))



def connect():
    access_token = "560167889-WlLRCzZ6UQ1EOlJo9Gc5dbMmFmgRU1CAUoxxdnoP"
    access_token_secret = "5C3GvXn8rO4rJt0IyBZShS14AqHoFgZx5Fhfecnm8PV2G"
    consumer_key = "waZeDptep8tQeTU4G7N5aUWnL"
    consumer_secret = "zSdiNnIJAMZtdHYzzsT90LI3aI0CWNXDCHwTxTvNRw5SE8f0Mo"
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api
    if not api:
        print("Can not connect to the Twitter API")
def analyze(text, fol):
    sentence = []
    predictList = []
    sentence.append(1)
    sentence.append(1)
    sentence.append(1)
    sentence.append(1)
    stop = set(stopwords.words('english'))
    tweetContext = word_tokenize(text)
    print(tweetContext)
    print('class 1',dic['word'][dic['class'] == '1'].count())
    print('class 2', dic['word'][dic['class'] == '2'].count())
    print('class 3', dic['word'][dic['class'] == '3'].count())
    print('class 4', dic['word'][dic['class'] == '4'].count())
    for w in tweetContext:
        if w not in stop:
            print(w, dic['word'][dic['class'] == '1'][dic['word'] == w].count(),
                  dic['word'][dic['class'] == '2'][dic['word'] == w].count(),
                  dic['word'][dic['class'] == '3'][dic['word'] == w].count(),
                  dic['word'][dic['class'] == '4'][dic['word'] == w].count())
            for k in range(1, 5):
                sentence[k - 1] = sentence[k - 1] * (
                            (dic['word'][dic['class'] == str(k)][dic['word'] == w].count() + 1) / dic['word'][
                        dic['class'] == str(k)].count())
                print(sentence[k - 1])

    for g in range(0, 4):
        print(' Probability of Class ', g + 1, sentence[g] / (sentence[0] + sentence[1] + sentence[2] + sentence[3]))
        predictList.append(sentence[g] / (sentence[0] + sentence[1] + sentence[2] + sentence[3]))
    print('predicted class and its probability value :', predictList.index(max(predictList)) + 1, max(predictList))
    rawSucces = data['score'][data['class'] == str(predictList.index(max(predictList)) + 1)].mean()*100
    succes = rawSucces/(3052982/int(fol))
    print('Number of user to reach with this tweet : ', round(succes, 0))

def getFol(api):
    acc = ['MaisonValentino', 'CHANEL', 'Prada', 'gucci', 'Coach', 'TommyHilfiger', 'UnderArmour', 'nike', 'VANS_66',
           'PUMA', 'LEVIS', 'LACOSTE', 'Converse', 'CalvinKlein', 'adidas']
    followerCounts = []
    for a in acc:
        user = api.get_user(a)
        followerCounts.append(user.followers_count)
    return followerCounts

#api = connect()
#fList = getFol(api)
#print(sum(fList)/len(fList))


#manuel tweet testing



#fol = input("enter follower count:")
#text = input("enter tweet:")
#analyze(text, fol)
