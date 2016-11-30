import json
def fmid(num):
    return '%03d' % num

data = []
for i in range(1, 152):
    with open('../py_output_json/DA0/'+fmid(i)+'.json', 'r') as latlng_file:
        data = json.load(latlng_file)
        print(len(data))

with open('../py_output_json/DA0_map_overview.json', '+w') as f:
    line = json.dumps(data)
    f.write(line)

