"""Data from GeoJSON Format"""
from pathlib import Path
import json
import plotly.express as px
#read data as string and convert to python object
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)
#examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']
#extracting date from our readable data file
mags, lons, lats = [], [], [] #empty lists to store mags, lons, and lats
#for all dictionaries in the file, extract the magnitude and append to mags
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
#plot the data as a world map
title = 'Global Earthquakes' #create variable for the title
#call scatter_geo() to lay the coordinates over a world map
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags, color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',)
fig.show()
    
