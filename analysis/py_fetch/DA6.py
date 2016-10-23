"""DA6:localTime"""
import csv
import json
with open('extracted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    dict_ans = {}
    for row in reader:
        dict_ans.setdefault(row["pokemonId"], {"Monday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "Tuesday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "Wednesday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "Thursday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "Friday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "Saturday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "Sunday":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}) #set default

with open('extracted_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        #count in csv file
        #format 2016-09-08T03:57:45 11-12
        if i["appearedDayOfWeek"] == "Monday":
            dict_ans[i["pokemonId"]]["Monday"][int(i["appearedLocalTime"][11:13])] += 1
        elif i["appearedDayOfWeek"] == "Tuesday":
            dict_ans[i["pokemonId"]]["Tuesday"][int(i["appearedLocalTime"][11:13])] += 1
        elif i["appearedDayOfWeek"] == "Wednesday":
            dict_ans[i["pokemonId"]]["Wednesday"][int(i["appearedLocalTime"][11:13])] += 1
        elif i["appearedDayOfWeek"] == "Thursday":
            dict_ans[i["pokemonId"]]["Thursday"][int(i["appearedLocalTime"][11:13])] += 1
        elif i["appearedDayOfWeek"] == "Friday":
            dict_ans[i["pokemonId"]]["Friday"][int(i["appearedLocalTime"][11:13])] += 1
        elif i["appearedDayOfWeek"] == "Saturday":
            dict_ans[i["pokemonId"]]["Saturday"][int(i["appearedLocalTime"][11:13])] += 1
        elif i["appearedDayOfWeek"] == "Sunday":
            dict_ans[i["pokemonId"]]["Sunday"][int(i["appearedLocalTime"][11:13])] += 1


with open('DA6.json', 'w') as f:
    json.dump(dict_ans, f)