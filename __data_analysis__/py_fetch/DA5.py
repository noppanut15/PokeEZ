"""
Output:DA5.json
collect top 5 of pokemon that spawned before the pokemonId then export to json format
{"pokemonId": {"pokemonId": numbers, "pokemonId": numbers, ... "pokemonId", numbers}}

**Example**
{"001": {"002": 25, "003":1, "004":15, ...}, ...........}
"""
import json as js
import pandas as pd
data = pd.read_csv('~/Desktop/PokeEZResource/data/extracted_data.csv').set_index('pokemonId')
json = {}
for index, row in data.iterrows():
    key = str('%03d' % index)
    if key not in json:
        json[key] = {}
    for i in range(1, 152):
        co_poke_id = '%03d' % i
        idx = 'cooc_' + str(i)
        if row[idx]:
            if co_poke_id not in json[key]:
                json[key][co_poke_id] = 1
            else:
                json[key][co_poke_id] += 1
for key in json:
    tmp_dict = json[key]
    top_5keys = sorted(tmp_dict, key=tmp_dict.get, reverse=True)
    top_5keys = top_5keys[:min(5, len(top_5keys))]
    new_dict = {}
    for i in top_5keys:
        new_dict[i] = tmp_dict[i]
    json[key] = new_dict
with open("DA5.json","w") as f:
    js.dump(json, f)
