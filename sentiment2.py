from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier 
from bagofwords_dict import *

with open('train_sent_final.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

[exciting, controversy, rain]=exc_con_rain()


up_down= ['but', 'although']
    
def feats(document): 
    document= document.lower()
    sent_list=document.split(".")
    pos=0
    neg=0
    neu=0
    more_neutral = 0
    exciting_count=0
    controversy_count=0
    rain_count=0
    up_down_count=0


    for sent in sent_list:
        word_list=[]
        label = cl.classify(sent)
        if label == "pos":
            pos = pos + 1
        elif label == "neg":
            neg = neg + 1
        elif label == "neu":
            neu = neu + 1
        word_list=sent.split(" ")
        for word in word_list:
            if word in exciting:
                exciting_count = exciting_count +1
            if word in controversy:
                controversy_count = controversy_count +1
            if word in rain:
                rain_count = rain_count +1
            if word in up_down:
                up_down_count= up_down_count+1
            
    if neu > pos and neu > neg:
        more_neutral = neu
    
    if neg != 0:
        ratio = pos/neg
        return ratio, exciting_count, controversy_count, rain_count, up_down_count 
    else:
        return pos, exciting_count, controversy_count, rain_count, up_down_count 
    

