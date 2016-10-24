"""
Output:DA1.json
collect top 10 of spawning area for each pokemon then export to json format
{"pokemonId": {"state1": numbers of pokemons, "state2": numbers of pokemons, ... "state3", numbers of pokemons}}


**Example**

 {"001": {"LA": 25, "GA": 2 , . . .}, "002": {"LA": 5, "GA": 12 , . . .}, ... "151": {"LA": 55, "GA": 1 , . . .}}

"""
import json as js
import pandas as pd
data = pd.read_csv('./PATH/TO/DATA.csv').set_index('pokemonId')
json = {}
for index, row in data.iterrows():
    key = str('%03d' % index)
    if key not in json:
        json[key] = {}
    city = row['city']
    if city not in json[key]:
        json[key][city] = 1
    else:
        json[key][city] += 1
for key in json:
    tmp_dict = json[key]
    top_5keys = sorted(tmp_dict, key=tmp_dict.get, reverse=True)
    top_5keys = top_5keys[:min(5, len(top_5keys))]
    new_dict = {}
    for i in top_5keys:
        new_dict[i] = tmp_dict[i]
    json[key] = new_dict
with open("DA1.json","w") as f:
    js.dump(json, f)
