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
            pos= pos+1
        elif label == "neg":
            neg= neg+1
        elif label == "neu":
            neu= neu+1
    return pos,neg,neu
