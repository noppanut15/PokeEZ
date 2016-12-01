# PokeEZ
PokeEZ is a web application that shows statistics of each Pokemon appeared in the Americas.

## Running the App

### Requirement
1. Python >= 3.4.x (https://www.python.org/download/)
2. Django (https://www.djangoproject.com/download/)
3. Pygal (http://www.pygal.org)


### Run Server
Run command
```
# Default port is 8000 and online on http://localhost/
python pokeez.py runserver <port>
```

### Data Analysis
Source code: `/__data_analysis__/py_fetch`

Raw Output in JSON: `/__data_analysis__/py_output_json`

Filename explanation:

1. `DA0` => Collect position data from raw CSV to each pokemon's collection in JSON. (For Google Heatmap in analytic page: `/analytic/xxx`)
2. `DA1` => Found in top 5 Cities (in times)
3. `DA2` => Time of the day of a sighting (in %)
4. `DA3` => How urban is location where pokemon appeared (Levels of Urban-Rural in %)
5. `DA4` => Weather type during a sighting (in %)
6. `DA5` => Top 5 Pokemon that appeared before ___ *(pokemon's name)* ____ (in %)
7. `DA6` => Exact time of a sighting (local time)
8. `DA_final` => Merge `DA1` - `DA6` to each pokemon's collection.
9. `OW0` => Collect all position records in to one JSON file. (For visualization in a Overview page `/overview`)
10. `OW1` => Find Top 5 Min-Max Population. (For visualization in a Overview page `/overview`)

### Special Thanks

1. Kaggle (https://www.kaggle.com/semioniy/predictemall)
2. Bootstrap (http://getbootstrap.com)
3. jQuery UI - Autocomplete (https://jqueryui.com/autocomplete/)
4. Google Heatmaps (https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap)
5. Django (https://www.djangoproject.com/)
6. Pygal (http://pygal.org/)
7. Pandas (http://pandas.pydata.org/)
