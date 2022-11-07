#make a random function that gives unique alphanumeric values
import random
import string
import json
def random_function2():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
with open('src.py/eng.json','r',encoding='utf-8') as f:
    print('eng.json set')
    print('loading data...')
    data = json.load(f)
    print('data loaded')
    with open('encoded.eng.json','w',encoding='utf-8') as f:
        print('writing data...')
        for i in data.keys():
            data[i] = random_function2()
        json.dump(data,f,indent=4)
        print('data written')