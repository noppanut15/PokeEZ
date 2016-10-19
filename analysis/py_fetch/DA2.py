"""DA2:time"""
import csv
with open('extracted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_ans = {}
    for row in reader:
        dict_ans.setdefault(row["pokemonId"], {"morning":0, "afternoon":0, "evening":0, "night":0}) #set default

with open('extracted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        #count in csv file
        if i["appearedTimeOfDay"] == "morning":
            dict_ans[i["pokemonId"]]["morning"] += 1
        elif i["appearedTimeOfDay"] == "afternoon":
            dict_ans[i["pokemonId"]]["afternoon"] += 1
        elif i["appearedTimeOfDay"] == "evening":
            dict_ans[i["pokemonId"]]["evening"] += 1
        elif i["appearedTimeOfDay"] == "night":
            dict_ans[i["pokemonId"]]["night"] += 1
    print(dict_ans)