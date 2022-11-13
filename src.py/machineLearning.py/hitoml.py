import json
import os
from deep_translator import GoogleTranslator

with open("src.py/eng.json","r",encoding="utf-8") as f:
    data = json.load(f)
cnt= 0
a=[] 
b=0
print("started")
for i in data.keys():
    a.append(i)
    cnt += 1
    if cnt == 1000:
        for i in a: 
            print(i,end=" ")
            
        b = 0 
        cnt = 0
        a = []
        break
print("done")


#
# regex for exact match of words
# word =  