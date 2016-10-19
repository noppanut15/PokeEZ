"""DA4:weather"""
import csv
import json
with open('extracted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_ans = {}
    for row in reader:
        dict_ans.setdefault(row["pokemonId"], {"fog":0, "clear-night":0, "partly-cloudy-night":0, "partly-cloudy-day":0, "cloudy":0, "clear-day":0, "rain":0, "wind":0}) #set default

with open('extracted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        #count in csv file
        if i["weatherIcon"] == "fog":
            dict_ans[i["pokemonId"]]["fog"] += 1
        elif i["weatherIcon"] == "clear-night":
            dict_ans[i["pokemonId"]]["clear-night"] += 1
        elif i["weatherIcon"] == "partly-cloudy-night":
            dict_ans[i["pokemonId"]]["partly-cloudy-night"] += 1
        elif i["weatherIcon"] == "partly-cloudy-day":
            dict_ans[i["pokemonId"]]["partly-cloudy-day"] += 1
        elif i["weatherIcon"] == "cloudy":
            dict_ans[i["pokemonId"]]["cloudy"] += 1
        elif i["weatherIcon"] == "clear-day":
            dict_ans[i["pokemonId"]]["clear-day"] += 1
        elif i["weatherIcon"] == "rain":
            dict_ans[i["pokemonId"]]["rain"] += 1
        elif i["weatherIcon"] == "wind":
            dict_ans[i["pokemonId"]]["wind"] += 1

with open('DA4.json', 'w') as f:
    json.dump(dict_ans, f)