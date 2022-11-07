import json
from sys import hash_info
class eng:
    def __init__(self):
        self.lang = 'eng'
        self.data = None
        with open('src.py/eng.json','r',encoding='utf-8') as f:
            self.data = json.load(f)

    def isword(self,word):
        a = word.split()
        b = ()
        if len(a) == 1:
            return word in self.data.keys()
        else:
            for i in enumerate(a):
                print(i)
                if i[1] in self.data.keys():
                    b += ((True,i[0],i[1]),)
                else:
                    b += ((False,i[0],i[1]),)
            return b
class hindi:
    def __init__(self):
        self.lang = 'hindi'
        self.data = None
        with open('src.py/hin.json','r',encoding='utf-8') as f:
            self.data = json.load(f)
    def isword(self,word):
        a = word.split()
        b = ()
        if len(a) == 1:
            return word in self.data.keys()
        else:
            for i in enumerate(a):
                print(i)
                if i[1] in self.data.keys():
                    b += ((True,i[0],i[1]),)
                else:
                    b += ((False,i[0],i[1]),)
            return b

