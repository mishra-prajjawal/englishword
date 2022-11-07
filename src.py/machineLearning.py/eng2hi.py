from deep_translator import GoogleTranslator
import json 
with open('./encoded.eng.json','r',encoding='utf-8') as f:
    data = json.load(f)
    a ={}
    print("program started")
    for i in data.keys():
        a[data[i]] = GoogleTranslator(source='en', target='hi').translate(i)
        print(a)
    with open('./encoded.hi.json','w',encoding='utf-8') as f:

        json.dump(a,f,indent=4)
    print("program ended")

