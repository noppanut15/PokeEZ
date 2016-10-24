import csv
def fmid(num):
    return '%03d' % num

us_map = {'Denver': 'CO', 'Detroit': 'MI', 'Los_Angeles': 'CA', 'Mexico_City': 'NM', 'Monterrey': 'NM', 'New_York': 'NY',
'Phoenix': 'AZ', 'Puerto_Rico': 'PR', 'Sao_Paulo': 'PW'}
for i in range(1, 152):
    with open('extracted_data.csv') as csvfile:
        data = {}
        check_dup = set()
        with open('../py_output_json/DA0/'+fmid(i)+'.csv', '+w') as f:
            line = 'states,amount\n'
            f.write(line)
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(i, row['pokemonId'], row['city'])
                # data[fmid(row['pokemonId'])][row]
                if row['city'] not in us_map:
                    continue
                if row['pokemonId'] == str(i):
                    if us_map[row['city']] in check_dup:
                        data[us_map[row['city']]] += 1
                    else:
                        check_dup.add(us_map[row['city']])
                        data[us_map[row['city']]] = 1
            for key, value in sorted(data.items()):
                line = str(key) + ',' + str(value) + '\n'
                f.write(line)
            f.closed
            print('Exported >>> %d of 151' % i)
        csvfile.closed
