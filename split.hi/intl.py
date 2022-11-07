import json  
with open("split.hi/1.hi.txt","r",encoding="utf-8") as f:
    data = f.read()
    #split the data
    data = data.split("\n")
    print(data)

with open("split.hi/1.hi.json","w",encoding="utf-8") as f:
   
    for i in data: 
        data_S = {} 
        data_S[i] =  1
        
    json.dump(data,f,indent=4,ensure_ascii=False)