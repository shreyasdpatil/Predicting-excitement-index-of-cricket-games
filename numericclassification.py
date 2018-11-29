#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:29:44 2018

@author: lubdhapimpale
"""
import pandas as pd
#from sentiment import *
from score import *
from sentiment import pred_train, true_train, pred_test, true_test

pred_train= pd.DataFrame(pred_train)
pred_test= pd.DataFrame(pred_test)
true_train= pd.DataFrame(true_train)
true_test= pd.DataFrame(true_test)

data = pd.read_csv('Shreyasdata.csv')
score= pd.DataFrame(data.score)
match_type= pd.DataFrame(data.match_type)
for_score= pd.concat([score,match_type], axis=1)
f1=[]
for i in range(len(for_score)):
    f1.append(get_score(for_score.iloc[i,0],for_score.iloc[i,1]))
f1= pd.DataFrame(f1)
x_train= pd.concat([pred_train,f1],axis=1)
y_train= data.label


data_t = pd.read_csv('Sarveshdata.csv')
score_t= pd.DataFrame(data_t.score)
match_type_t= pd.DataFrame(data_t.match_type)
for_score_t= pd.concat([score_t,match_type_t], axis=1)
f2=[]
for i in range(len(for_score_t)):
    f2.append(get_score(for_score_t.iloc[i,0],for_score_t.iloc[i,1]))
f2 = pd.DataFrame(f2)
x_test= pd.concat([pred_test,f2],axis=1)
y_test= data_t.label


from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
model = dtc.fit(x_train, y_train)
y_pred = model.predict(x_test)

#from sklearn import datasets
#from sklearn.ensemble import RandomForestClassifier
#rfc = RandomForestClassifier()
#model = rfc.fit(x_train, y_train)
#y_pred = model.predict(x_test)

#from sklearn import datasets
#from sklearn.svm import SVC
#svc = SVC()
#model = svc.fit(x_train, y_train)
#y_pred = model.predict(x_test)

#from sklearn import datasets
#from sklearn.naive_bayes import GaussianNB
#nb = GaussianNB()
#model = nb.fit(x_train, y_train)
#y_pred = model.predict(x_test)


count=0
for i in range(len(y_pred)):
    if y_pred[i] == y_test[i]:
        count= count+1
print('accuracy_final',count/len(y_pred))