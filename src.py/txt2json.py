from concurrent.futures import process
import json
with open('src.py/hin.txt','r',encoding="utf-8") as f: 
    print('loading data')
    data = f.readlines()
    main_data = [] 
    print('data loaded')
    print('removal of new line')
    for i in data:
        main_data.append(i.replace("\n", ""))
    print('new line removed')
    with open('src.py/hin.json','r+',encoding="utf-8") as frc: 
        print('processing...')
        a = json.load(frc)
        print('process started...')
        for i in main_data:
            a[i] = 1
        frc.seek(0)
        json.dump(a,frc,indent=4,ensure_ascii=False,)
        frc.truncate()
        print('work done!')
    
