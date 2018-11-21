import pandas as pd
word_dict={}
sent_list_list=[]
sent_list=[]
data= pd.read_excel("/Users/lubdhapimpale/Desktop/dataset-cricketmatchsummary.xlsx")
data.columns=["summary","score","type","teams","label"]
for i in data.summary:
    sent_list_list.append(i.split("."))
    
sent_list =[j for i in sent_list_list for j in i]

for sentence in sent_list:
    k= sentence.split(" ")
    for word in k:
        if word not in word_dict:
            word_dict[word]= 1
        else:
            word_dict[word] = word_dict[word]+1  
    
