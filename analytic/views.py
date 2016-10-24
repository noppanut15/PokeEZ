from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
import os
import pygal
import operator
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def detail(request, pokemon_id):
    #try:
    file_path = os.path.join(BASE_DIR, 'PokeEZ/static/db/pokedex-info.json')
    with open(file_path) as data_file:
        pokedex_info = json.load(data_file)
    file_path = os.path.join(BASE_DIR, 'PokeEZ/static/db/pokemon/'+pokemon_id+'.json')
    with open(file_path) as data_file:
        db = json.load(data_file)
    # DA1 : Top 5 States
    chartDA1 = pygal.Bar(height=350)
    chartDA1.title = 'Found in top 5 Cities (in times)'
    for state, amount in sorted(db['DA1'].items(), key=operator.itemgetter(1), reverse=True):
        chartDA1.add(state, amount)
    chartDA1 = chartDA1.render_data_uri()
    #DA2: Period of time
    chartDA2 = pygal.Pie(half_pie=True, height=350)
    chartDA2.title = 'Time of the day of a sighting (in %)'
    chartDA2.value_formatter = lambda x: "%.2f" % x
    sum_DA2 = sum(db['DA2'].values())
    for time, amount in sorted(db['DA2'].items(), key=operator.itemgetter(1), reverse=True):
        chartDA2.add(time.title(), amount/sum_DA2*100)
    chartDA2 = chartDA2.render_data_uri()
    #DA3: Area (Urban -> Rural)
    chartDA3 = pygal.Radar(height=350)
    chartDA3.title = 'How urban is location where pokemon appeared (Levels of Urban-Rural in %)'
    chartDA3.value_formatter = lambda x: "%.2f" % x
    chartDA3.x_labels = ['Urban', 'Suburban', 'Midurban', 'Rural']
    sum_DA3 = sum(db['DA3'])
    chartDA3.add(pokedex_info[pokemon_id][0], [i/sum_DA3*100 for i in db['DA3']])
    chartDA3 = chartDA3.render_data_uri()
    # DA4 : Atmospheric conditions
    chartDA4 = pygal.Bar(height=350)
    chartDA4.title = 'Weather type during a sighting (in %)'
    chartDA4.value_formatter = lambda x: "%.2f" % x
    sum_DA4 = sum(db['DA4'].values())
    for weather, amount in db['DA4'].items():
        weather = weather.split('-')
        weather = ' '.join(weather)
        chartDA4.add(weather.title(), amount/sum_DA4*100)
    chartDA4 = chartDA4.render_data_uri()
    # DA5 : Top 5 Pokemon that appeared before.
    chartDA5 = pygal.Bar(height=350)
    chartDA5.title = 'Top 5 Pokemon that appeared before ' + pokedex_info[pokemon_id][0] + ' (in %)'
    chartDA5.value_formatter = lambda x: "%.2f" % x
    sum_DA5 = sum(db['DA5'].values())
    for pid, amount in sorted(db['DA5'].items(), key=operator.itemgetter(1), reverse=True):
        chartDA5.add(pokedex_info[pid][0], amount/sum_DA5*100)
    chartDA5 = chartDA5.render_data_uri()
    # DA6 : Punch card.
    chartDA6 = pygal.Dot(x_label_rotation=30, height=350)
    chartDA6.title = 'Exact time of a sighting (local time)'
    chartDA6.x_labels = ['12a', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12p', '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', '11p']
    try:
        chartDA6.add('Sunday', db['DA6']['Sunday'])
        chartDA6.add('Monday', db['DA6']['Monday'])
        chartDA6.add('Tuesday', db['DA6']['Tuesday'])
        chartDA6.add('Wednesday', db['DA6']['Wednesday'])
        chartDA6.add('Thursday', db['DA6']['Thursday'])
        chartDA6.add('Friday', db['DA6']['Friday'])
        chartDA6.add('Saturday', db['DA6']['Saturday'])
    except:
        chartDA6.add('Sunday', [])
        chartDA6.add('Monday', [])
        chartDA6.add('Tuesday', [])
        chartDA6.add('Wednesday', [])
        chartDA6.add('Thursday', [])
        chartDA6.add('Friday', [])
        chartDA6.add('Saturday', [])

    chartDA6 = chartDA6.render_data_uri()
    context = {
        'id': pokemon_id,
        'pokedex_info': pokedex_info[pokemon_id],
        'chartDA1': chartDA1,
        'chartDA2': chartDA2,
        'chartDA3': chartDA3,
        'chartDA4': chartDA4,
        'chartDA5': chartDA5,
        'chartDA6': chartDA6,
    }
    return render(request, 'analytic.html', context)
    #except:
        #return HttpResponseRedirect('/')
