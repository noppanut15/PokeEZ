import json
def fmid(num):
    return '%03d' % num
"""
for i in range(1, 152):
    with open('../py_output_json/DA0_map_overview.json') as latlng_file:
        data = []
        with open('../py_output_json/DA0/'+fmid(i)+'.json', '+w') as f:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['pokemonId'] == str(i):
                    data.append({'lat': row['latitude'], 'lng': row['longitude']})
            line = json.dumps(data)
            f.write(line)
            f.closed
            print('Exported >>> %d of 151' % i)
        csvfile.closed
"""

with open('../py_output_json/DA0/001.json', '+w') as latlng_file:
    data = json.load(latlng_file)
    print(data)