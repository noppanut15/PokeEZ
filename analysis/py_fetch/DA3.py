"""
Output:DA3.json
collect spawning area of each pokemon then export to json format
{"Id": [Numbers of urban if True, suburban if True, midurban if True,rural if True]}


**Example**

 {"001": [25, 2, 0, 0], ... , "151": [125, 0, 1, 51]}

"""
import json as js
import pandas as pd
data = pd.read_csv('./data/extracted_data.csv').set_index('pokemonId')
json = {}
for index, row in data.iterrows():
    key = str('%03d' % index)
    #print(key,row['urban'],row['suburban'],row['midurban'],row['rural'])
    if key not in json:
        json[key] = [0, 0, 0, 0]
    if row['urban']:
        json[key][0] += 1
    if row['suburban']:
        json[key][1] += 1
    if row['midurban']:
        json[key][2] += 1
    if row['rural']:
        json[key][3] += 1
with open("DA3.json","w") as f:
    js.dump(json, f)