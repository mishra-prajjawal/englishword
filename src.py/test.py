import json
with open("src.py/pl.txt", "r") as f:
    data = []
    for line in f:
        data.append(line.split("\n")[0])

with open("poisels.js","w") as frc:
    frc.write("let keyson = ")
    json.dump(data,frc,indent=4)
    frc.write(";")
    frc.close()
