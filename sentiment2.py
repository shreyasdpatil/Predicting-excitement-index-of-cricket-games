from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier 

with open('train_sent_final.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

def pos_neg(document):    
    sent_list_list=[]
    sent_list_list.append(document.split("."))
    sent_list =[j for i in sent_list_list for j in i]
    pos=0
    neg=0
    neu=0
    for sent in sent_list:
#        print('sent',sent)
        label = cl.classify(sent)
        if label == "pos":
            pos = pos+1
        elif label == "neg":
            neg = neg+1
        elif label == "neu":
            neu = neu+1
    return pos,neg,neu


#
#from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
#from textblob.classifiers import NaiveBayesClassifier 
#
#with open('train_sent_final.json', 'r') as fp:
#    cl = NaiveBayesClassifier(fp, format="json")
#
#def pos_neg(document):    
#    sent_list_list=[]
#    sent_list_list.append(document.split("."))
#    sent_list =[j for i in sent_list_list for j in i]
#    pos=0
#    neg=0
#    neu=0
#    more_neutral = 0
#    for sent in sent_list:
#        label = cl.classify(sent)
#        if label == "pos":
#            pos = pos + 1
#        elif label == "neg":
#            neg = neg + 1
#        elif label == "neu":
#            neu = neu + 1
#
## Ratio of positive to negative
#    if neu > pos and neu > neg:
#        more_neutral = neu
#    
#    
#    
#    if neg != 0:
#        ratio = pos/neg
#        return more_neutral, ratio 
#    else:
#        return more_neutral, pos
#    
#    if ratio == 1:
#        ratio_neutral.append(ratio)
#        print("ratio", ratio)
#        return ratio_neutral
#    elif ratio > 1:
#        ratio_neutral.append(ratio)
#        print("ratio", ratio)
#        return ratio_neutral
#    elif ratio < 1:
#        ratio_neutral.append(ratio)
#        print("ratio", ratio)
#        return ratio_neutral

