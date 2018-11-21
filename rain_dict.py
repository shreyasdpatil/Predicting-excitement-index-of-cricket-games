# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:10:31 2018

@author: Sarvesh
"""
from nltk.corpus import wordnet as wn

def get_all_hyponyms(word, pos=None):
    hypo=[]
    for ss in wn.synsets(word, pos=pos):
            for hyp in ss.hyponyms():
                for lemma in hyp.lemma_names():
                    hypo.append(str(lemma))
    return hypo


def get_all_synsets(word, pos=None):
    sset=[]
    for ss in wn.synsets(word):
        for lemma in ss.lemma_names():
             sset.append(str(lemma))
    return sset

rain_dict={}
h=[]
s=get_all_synsets('rain')
for word in s:
    if word not in rain_dict.keys():
        rain_dict[word]=1
    
for word in s:
    h=get_all_hyponyms(word)
    for w in h:
        if w not in rain_dict.keys():
            rain_dict[w]=1
            
#all final words stored in rain_dict
            
            
    
    