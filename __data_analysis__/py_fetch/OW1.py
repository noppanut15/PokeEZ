import json
def fmid(num):
    return '%03d' % num

population = {}
for i in range(1, 152):
    with open('../py_output_json/DA0/'+fmid(i)+'.json', 'r') as latlng_file:
        data = json.load(latlng_file)
        population[fmid(i)] = len(data)
population = sorted(population.items(), key=lambda kv: kv[1])
print("Top 5 Hard")
for pid, number in population[9:9+5]:
    print(pid, number)
print("\nTop 5 Easy")
for pid, number in population[-1:-6:-1]:
    print(pid, number)

