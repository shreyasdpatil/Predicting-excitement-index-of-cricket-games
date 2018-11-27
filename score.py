# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:06:23 2018

@author: Sarvesh
"""



def get_score(score,match_type):
    score=score.strip().split()
    
    if len(score)==2 and score[1]=="tied":
        return 10
    
    if len(score)==5:
        if "wkts"==score[4]:
            posw=score.index("wkts")
            nwkts=int(score[posw-1])
            if nwkts <4:
                return 10
            if nwkts>=4 and nwkts<=7:
                return 5
            if nwkts>=8:
                return 3
            
    
        if "runs"==score[4]:
            posr=score.index("runs")
            nruns=int(score[posr-1])
            
            if match_type=="T20":
                if (nruns>1 and nruns<=5):
                    return 10
                if (nruns>5 and nruns<=10): 
                    return 7
                if (nruns>10 and nruns<=20): 
                    return 5
                if nruns>20:
                    return 1
                
            if match_type=="ODI":
                if nruns<10:
                    return 10
                if nruns>10 and nruns<=25:
                    return 7
                if nruns>25 and nruns<=40:
                    return 5
                if nruns>40:
                    return 1
                
            
            

x=get_score("SA won by 5 runs","ODI")