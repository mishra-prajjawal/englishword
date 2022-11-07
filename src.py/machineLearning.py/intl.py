import json 
import re 
from deep_translator import GoogleTranslator
def intl(word,action,lang):
    with open("src.py/machineLearning.py/encoded.eng.json","r",encoding="utf-8") as f:
        data = json.load(f)
    word = word.split()
    with open('word.xlx','w',encoding='utf-8') as fa:
        print('writing data...')
        for i in data.keys():
            fa.write(i)
            fa.write('\n')
        print('data written')
    nlp = []
    for i in word:
        if i in data.keys():
            nlp.append(data[i])
    if nlp==[]:
        return 'invalid wordset'
    else:
        return nlp
   
a = intl("sex world","encode","eng")
print(a)

