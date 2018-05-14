import json
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open("dictionary.json", encoding='utf8') as jsonFile:
    dic = json.load(jsonFile)
dic = pd.DataFrame(dic)

with open("classifiedData.json", encoding='utf8') as jsonFile:
    data = json.load(jsonFile)
data = pd.DataFrame(data)

#get stopwords from nltk library
stop = set(stopwords.words('english'))

#sentence list is for containing probability rates for the sentence for each class, since begin and continiue by multiplying
sentence = []
normalizeList = []
predictionList = []
sentence.append(1)
sentence.append(1)
sentence.append(1)
sentence.append(1)
for i in range(int(data.shape[0]*80/100)+1, int(data.shape[0])):
    tweetContext = word_tokenize(data.loc[i]['text'])
    print(tweetContext)
    for w in tweetContext:
        if w not in stop:
            #print(w, dic['word'][dic['class'] == '1'][dic['word'] == w].count(), dic['word'][dic['class'] == '2'][dic['word'] == w].count(), dic['word'][dic['class'] == '3'][dic['word'] == w].count(), dic['word'][dic['class'] == '4'][dic['word'] == w].count())
            for k in range(1,5):
                sentence[k-1] = sentence[k-1] * ((dic['word'][dic['class'] == str(k)][dic['word'] == w].count() + 1) / dic['word'][dic['class'] == str(k)].count())
                #print(sentence[k-1])

    for g in range(0, 4):
        #print(' Probability of Class ', g+1, sentence[g] / (sentence[0] + sentence[1] + sentence[2] + sentence[3]))
        normalizeList.append(sentence[g] / (sentence[0] + sentence[1] + sentence[2] + sentence[3]))
    print('predicted class and its probability value :', normalizeList.index(max(normalizeList))+1, max(normalizeList))
    predictionList.append({'actual': data.loc[i]['class'] , 'prediction': normalizeList.index(max(normalizeList))+1})
    #print(normalizeList.index(max(normalizeList))+1,data.loc[i]['class'])
    del sentence[:]
    del normalizeList[:]
    sentence.append(1)
    sentence.append(1)
    sentence.append(1)
    sentence.append(1)
with open("summary.json", 'w', encoding='utf8') as t:
    json.dump(predictionList, t, ensure_ascii=False)

        #dic['word'][dic['class'] == '1'][dic['word'] == w].count() / dic['word'][dic['class'] == '1'].count()






#calculating probabilities using naive bayes, assuming indipendence



