def get_score(score,match_type):
#    score=score.strip().split()
#    
#    if len(score)==2 and score[1]=="tied":
#        return 10
#
#    
#    elif "wkts"==score[4] or score[4]=="wickets" or "wkt"==score[4]:
#        posw=score.index(score[4])
#        nwkts=int(score[posw-1])
#        if nwkts <4:
#            return 10
#        if nwkts>=4 and nwkts<=7:
#            return 5
#        if nwkts>=8:
#            return 3
#
#
#    elif "runs"==score[4] or "run"==score[4]:
#        posr=score.index(score[4])
#        nruns=int(score[posr-1])
#        
#        if match_type=="T20":
#            if (nruns>1 and nruns<=5):
#                return 10
#            if (nruns>5 and nruns<=10): 
#                return 7
#            if (nruns>10 and nruns<=20): 
#                return 5
#            if nruns>20:
#                return 1
#            
#        if match_type=="ODI":
#            if nruns<10:
#                return 10
#            if nruns>10 and nruns<=25:
#                return 7
#            if nruns>25 and nruns<=40:
#                return 5
#            if nruns>40:
#                return 1
#            
#    elif "wkts"==score[5] or "wickets"==score[5] or "wkt"==score[5]:
#        posw=score.index(score[5])
#        nwkts=int(score[posw-1])
#        if nwkts <4:
#            return 10
#        if nwkts>=4 and nwkts<=7:
#            return 5
#        if nwkts>=8:
#            return 3
#    
#    elif "runs"==score[5] or "run"==score[5]:
#        posr=score.index(score[5])
#        nruns=int(score[posr-1])
#        
#        if match_type=="T20":
#            if (nruns>1 and nruns<=5):
#                return 10
#            if (nruns>5 and nruns<=10): 
#                return 7
#            if (nruns>10 and nruns<=20): 
#                return 5
#            if nruns>20:
#                return 1
#            
#        if match_type=="ODI":
#            if nruns<10:
#                return 10
#            if nruns>10 and nruns<=25:
#                return 7
#            if nruns>25 and nruns<=40:
#                return 5
#            if nruns>40:
#                return 1
                
    if "tie" in score:
        return 10
    elif "wkt" in score:
        score=score.strip().split()
        for i in score:
            if i.isdigit():
                nwkts= int(i)
            
        if nwkts <4:
            return 10
        if nwkts>=4 and nwkts<=7:
            return 5
        if nwkts>=8:
            return 3
    elif "wicket" in score:
        score=score.strip().split()
        for i in score:
            if i.isdigit():
                nwkts= int(i)      
        if nwkts <4:
            return 10
        if nwkts>=4 and nwkts<=7:
            return 5
        if nwkts>=8:
            return 3
    elif "run" in score:
        score=score.strip().split()
        for i in score:
            if i.isdigit():
                nruns= int(i)
        if "T20" in match_type:
            if (nruns>=1 and nruns<=5):
                return 10
            if (nruns>5 and nruns<=10): 
                return 7
            if (nruns>10 and nruns<=20): 
                return 5
            if nruns>20:
                return 1
            
        if "ODI" in match_type:
            if nruns<=10:
                return 10
            if nruns>10 and nruns<=25:
                return 7
            if nruns>25 and nruns<=40:
                return 5
            if nruns>40:
                return 1
            
#        if "Test" in match_type:
#            if nruns<=20:
#                return 10
#            if nruns>20 and nruns<=30:
#                return 7
#            if nruns>30 and nruns<=40:
#                return 5
#            if nruns>40:
#                return 1
            

x=get_score("Bangladesh won by 1 run"," T20")