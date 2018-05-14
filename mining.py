# -*- coding: utf-8 -*-
import json
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np




 #get the data from json file thats been filled by collect.py
with open("mainData.json", encoding='utf8') as jsonFile:
    data = json.load(jsonFile)
data = pd.DataFrame(data)
#shuffle the records
data = data.sample(frac=1).reset_index(drop=True)
#we divide the score data in to 4 bins as 4 success stages of a tweet being bad, moderate, good and very good.
bins = [data['score'].describe()['min'], data['score'].describe()['25%'], data['score'].describe()['50%'], data['score'].describe()['75%'], data['score'].describe()['max']]
labels=['1','2','3','4']
data['star'] = pd.cut(data['score'],bins,labels=labels)

#frequency table for companies star rate
group = data.groupby(['company','star'])
#print(group['star'].count().unstack())

classifiedData = []
for i in range(0,data.shape[0]):
    text = data.loc[i]['text']
    star = data.loc[i]['star']
    score = data.loc[i]['score']
    company2 = data.loc[i]['company']
    id = data.loc[i]['id']
    classifiedData.append({'text': text, 'company': company2, 'score': score, 'class': star, })

with open("classifiedData.json", 'w', encoding='utf8') as c:
    json.dump(classifiedData, c, ensure_ascii=False)


BoW = []
dic = []
stop = set(stopwords.words('english'))
#running for only 80% of the data so the rest will be test data

for t in range(0, int(data.shape[0]*80/100)):
    tweetText = data.loc[t]['text']
    tweetStar = data.loc[t]['star']
    company = data.loc[t]['company']
    tweetContext = word_tokenize(tweetText)

    for w in tweetContext:
        if w not in stop:
                BoW.append(w)
                dic.append({'word': w, 'class': tweetStar, 'company': company})

#with open("dictionary.json", 'w', encoding='utf8') as d:
 #   json.dump(dic, d, ensure_ascii=False)



'''

print('number of words:',dic['word'].count())
print('number of unique words:',len(list(dic['word'].unique())))


group = dic.groupby(['word','star'])
x = group['star'].count()
x = pd.DataFrame(x)

#print(x['word'][x['word']=='aaron'])
'''