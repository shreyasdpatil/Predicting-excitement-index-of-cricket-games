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
#    for sent in sent_list:
##        print('sent',sent)
#        label = cl.classify(sent)
#        if label == "pos":
#            pos = pos+1
#        elif label == "neg":
#            neg = neg+1
#        elif label == "neu":
#            neu = neu+1
#    return pos,neg,neu



from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier 
from bagofwords_dict import *

with open('train_sent_final.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

[exciting, controversy,rain]=ex_co_rain()

lex=[]
lexicons= open("Cricket.tsv").read()
l= lexicons.split("\n")
for a in l:
    lex.append(a.split("\t"))
    
del lex[-1]
lex_words=[]
for t in range(len(lex)):
    lex_words.append(lex[t][0])
    
def pos_neg(document): 
    global lex
    global lex_words
    sent_list_list=[]
    sent_list=document.split(".")
    lex0=[]
#    sent_list =[j for i in sent_list_list for j in i]
    pos=0
    neg=0
    neu=0
    more_neutral = 0
    exciting_count=0
    controversy_count=0
    rain_count=0


    for sent in sent_list:
        word_list=[]


#        print('sent',sent)
#        print('type',type(sent))
        label = cl.classify(sent)
        if label == "pos":
            pos = pos + 1
        elif label == "neg":
            neg = neg + 1
        elif label == "neu":
            neu = neu + 1
        word_list=sent.split(" ")
#        print('wl',word_list)
        for word in word_list:
#            print('word',word)
            if word in exciting:
                exciting_count = exciting_count +1
            if word in controversy:
                controversy_count = controversy_count +1
            if word in rain:
                rain_count = rain_count +1
            if word in lex_words:
                index=lex_words.index(word)
                lex0.append([word,lex[index][1],lex[index][2]])


                
                
        

# Ratio of positive to negative
    if neu > pos and neu > neg:
        more_neutral = neu
    
    
    
    if neg != 0:
        ratio = pos/neg
        return more_neutral, ratio, exciting_count, controversy_count, rain_count, lex0 
    else:
        return more_neutral, pos, exciting_count, controversy_count, rain_count, lex0 
    


