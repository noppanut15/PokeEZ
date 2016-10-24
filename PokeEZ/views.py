from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
import os

def index(request):
    context = {
        'nav_pokedex': '',
        'nav_about': '',
    }
    return render(request, 'index.html', context)

def pokedex(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/db/pokedex-info.json')
    with open(file_path) as data_file:
        data = json.load(data_file)
    context = {
        'nav_pokedex': 'active',
        'nav_about': '',
        'infos': sorted(data.items()),
    }
    return render(request, 'pokedex.html', context)

def about(request):
    context = {
        'nav_pokedex': '',
        'nav_about': 'active',
    }
    return render(request, 'about-us.html', context)

def search_by_name(request):
    try:
        if request.method == 'POST':
            pokemon_name = request.POST['pokename']
            module_dir = os.path.dirname(__file__)  # get current directory
            file_path = os.path.join(module_dir, 'static/db/pokename_to_id.json')
            with open(file_path) as data_file:
                data = json.load(data_file)
            #return render(request, 'analytic.html', {'pokemon_id': data[pokemon_name]})
            return HttpResponseRedirect('/analytic/'+data[pokemon_name])
    except:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')
