from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd 
from sentiment2 import pos_neg


#Data = open("Sarvesh datacol.json", "r").read()
#xtrain = Data["Data"]
#ytrain = Data["Label"]
#x = pd.concat([xtrain, ytrain],axis=1)
def feat_extractor(document):
    feats = {}
    [pos,neg,neu] = pos_neg(document)
    feats["count_pos"] = pos
    feats["count_neg"] = neg
    feats["count_neu"] = neu
    return feats 

A = " If not for Jonker's feat on debut, this match was dead a long time ago. India's 172 might have divided opinions at the halfway stage but South Africa soon found that it shouldn't have. They were chasing an above par score on a pitch responsive to cutters and change of pace, something which conspired a dragged 52/2 from the hosts after 10 overs. A punt with Miller at the opening slot backfired, Klaasen didn't quite have this night to himself, and Duminy's 55 could have only taken them so far. "
#print(feat_extractor(A))
with open('Sarvesh datacol.json', 'r') as fp1:
    cl2 = NaiveBayesClassifier(fp1,feature_extractor=feat_extractor,  format="json")
#cl2 = NaiveBayesClassifier(Data, feature_extractor=feat_extractor, format="json")
blob = TextBlob(A, classifier=cl2)
print(blob.classify())



