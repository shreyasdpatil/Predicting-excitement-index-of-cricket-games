#from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
#from textblob.classifiers import NaiveBayesClassifier
#import pandas as pd 
#from sentiment2 import pos_neg
#
#def feat_extractor(document):
#    feats = {}
#    [pos,neg,neu] = pos_neg(document)
#    feats["count_pos"] = pos
#    feats["count_neg"] = neg
#    feats["count_neu"] = neu
#    return feats 
#
#
#
##A = "A comprhensive win for Pakistan but they have been made to work for the victory. A commendable show by Afghanistan in their first outing. Their players were spirited right until the last runs were scored and showed a very good attitude on the field. They were not intimidated by some of the big names in the Pakistan side and walk off with heads held high."
#with open('Shreyasdatacol.json', 'r') as fp1:
#    cl2 = NaiveBayesClassifier(fp1,feature_extractor=feat_extractor,  format="json")
#
#pred=[]
#test= pd.read_excel('sarvesh_datacol.xlsx') 
#true= test.Label
#for instance in test.Data:
#    blob = TextBlob(instance, classifier=cl2)
#    pred.append(int(float(blob.classify())))
#count=0
#for i in range(len(pred)):
#    if pred[i] == true[i]:
#        count= count+1
#print('accuracy',count/len(pred))
    
#print(cl2.accuracy(test, format='json'))
#blob = TextBlob(A, classifier=cl2)
#print(blob.classify())
#
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd 
from sentiment2 import pos_neg

#A = "From 71-0 in the 6th over to 149/9 in 20. Who would have imagined that when Shane Watson was toying around with the bowling? But credit to Sri Lanka, and Mendis in particular, for the stunning comeback. They came back from nowhere and choked Australia with spin to take the game, despite some late hitting from Cameron White"


def feat_extractor(document):
#    print('d', document) 
    feats = {}
    [more_neutral, pos_neg_ratio,exciting_count, controversy_count, rain_count,lex0] = pos_neg(document)
    feats["more_neutral"] = more_neutral
    feats["pos_neg_ratio"] = pos_neg_ratio
    feats["exciting"]= exciting_count
    feats["controversy"]= controversy_count
    feats["rain"]= rain_count 
#    for i in range(len(lex0)):
#        feats[lex0[i][0]+"_lex0"] = lex0[i][1]
#        feats[lex0[i][0]+"_lex1"] = lex0[i][2]
#    feats["closeness"]= document.score
#    feats["teams"]= document.team
#    feats["type"]= document.type[j]
#    print('d', document)
#    print('feats',feats)
    return feats 

global pred_train
global true_train
pred_train=[]
with open('Shreyasdata.json', 'r') as fp2:
    cl2 = NaiveBayesClassifier(fp2, feature_extractor=feat_extractor, format="json")

train = pd.read_excel('Shreyasdata.xlsx') 
true_train= train.label
for instance in train.text:
    blob = TextBlob(instance, classifier=cl2)
    pred_train.append(int(float(blob.classify())))
count=0
for i in range(len(pred_train)):
    if pred_train[i] == true_train[i]:
        count= count+1
print('accuracy_train',count/len(pred_train))

#test= open('Sarveshdata.json','r') 
#
#print('accuracy',cl2.accuracy(test, format='json'))
#test= open('Sarvesh datacol.json','r') 
#print(cl2.accuracy(test, format='json'))
#
#test = pd.read_excel("sarvesh datacol.xlsx")
#text = test["Data"]
#for i in text:
    
global pred_test
global true_test
pred_test=[]
test = pd.read_excel('Sarveshdata.xlsx') 
true_test= test.label
for instance in test.text:
    blob = TextBlob(instance, classifier=cl2)
    pred_test.append(int(float(blob.classify())))
count=0
for i in range(len(pred_test)):
    if pred_test[i] == true_test[i]:
        count= count+1
print('accuracy_test',count/len(pred_test))



#
#blob = TextBlob(A, classifier=cl2)
#print(blob.classify())
