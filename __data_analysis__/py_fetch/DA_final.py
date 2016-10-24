"""
This program will collect all data (from DA[1-6].json) and export to each pokemon data files.
"""
def idconv(pid):
    """This function will convert the Pokemon ID from *int to *str 3 digits. """
    return '%03d' % pid

import json
for pid in range(1, 152):
    pokemon_db = {}
    # DA1
    with open("../py_output_json/DA1.json","r") as da:
        rows = json.load(da)
        try:
            pokemon_db['DA1'] = rows[idconv(pid)]
        except:
            pokemon_db['DA1'] = {}
        da.closed
    with open("../py_output_json/DA2.json","r") as da:
        rows = json.load(da)
        try:
            pokemon_db['DA2'] = rows[str(pid)]
        except:
            pokemon_db['DA2'] = {}
        da.closed
    with open("../py_output_json/DA3.json","r") as da:
        rows = json.load(da)
        try:
            pokemon_db['DA3'] = rows[idconv(pid)]
        except:
            pokemon_db['DA3'] = {}
        da.closed
    with open("../py_output_json/DA4.json","r") as da:
        rows = json.load(da)
        try:
            pokemon_db['DA4'] = rows[str(pid)]
        except:
            pokemon_db['DA4'] = {}
        da.closed
    with open("../py_output_json/DA5.json","r") as da:
        rows = json.load(da)
        try:
            pokemon_db['DA5'] = rows[idconv(pid)]
        except:
            pokemon_db['DA5'] = {}
        da.closed
    with open("../py_output_json/DA6.json","r") as da:
        rows = json.load(da)
        try:
            pokemon_db['DA6'] = rows[str(pid)]
        except:
            pokemon_db['DA6'] = {}
        da.closed
    with open("../py_output_json/DA_final/" + idconv(pid) + ".json","w") as f:
        json.dump(pokemon_db, f)
        f.closed
    print("Exported >>> %d of 151" % pid)
