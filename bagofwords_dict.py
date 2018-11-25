# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:06:37 2018

@author: Sarvesh
"""

from nltk.corpus import wordnet as wn


def get_all_similar_tos(word, pos=None):
    sim_tos=[]
    for ss in wn.synsets(word):
            for sim in ss.similar_tos():
                for lemma in sim.lemma_names():
                    sim_tos.append(str(lemma))
    return sim_tos

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

#--------------------------------------------------------------------------------------------------------#
    

contro_dict={}
excite_dict={}
excite_google=['amazing','fantastic','exciting','dramatic','terrific']
contro_google=['controversy','controversial','arguable','vexed','argument','bickering',
               'difference','discussion','fuss','quarrel','row','beef','rumpus','dissention']
for words in excite_google:
    s=get_all_similar_tos(words)
    for w in s:
        if w not in excite_dict.keys():
            excite_dict[w]=1

for words in contro_google:
    s=get_all_similar_tos(words)
    for w in s:
        if w not in excite_dict.keys():
            contro_dict[w]=1

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
            

    
