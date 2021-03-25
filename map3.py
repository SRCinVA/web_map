import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# you need to create the function before you need it in the for loop below
def color_producer(elev):
    if elev <= 1000: # you cast them as ints but pass them as strings -- what the ...?
        return "green"
    if elev >= 1001 and elev <= 2000:
        return "orange"
    if elev >= 2001:
        return "red"

# Ardit's code
#  if elevation < 1000:
#      return 'green'
#  elif 1000 <= elevation < 3000:
#      return 'orange'
#  else:
#      return 'red'

map = folium.Map(location=[33.99,-77.5], zoom_start=6, tiles = "Stamen Terrain")

# another way to add children is a feature group
fgv = folium.FeatureGroup(name="Volcanoes") # for volcanoes

# we can add objects to that map. Multiple markers require multiple methods, or you can use a for loop:
# for coordinates in [[33.98, -77.6], [35.00, -77.6]]:
#   map.add_child(folium.Marker(location = coordinates, popup = "Greetings! I'm a marker.", icon=folium.Icon(color ="green")))

# the zip function lets you iterate over items from multiple separate lists
for lt,ln,el in zip(lat,lon,elev): # strangely, never got his type error; folium had trouble with floats for my code.
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " m", # need to pass <el> to color_producer()
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))
    # he took away 'folium.Icon' -- maybe that was a standard icon of some sort?
    # color = "grey" is for the outline of the dot.
    # nice that you can add radius to the dot.

fgp = folium.FeatureGroup(name="Population")  # for population

# to dispaly the data from the world.json file. The folium.GeoJson objects takes data attribute. 
# We give it a file object using open(world.json). We open it in read mode.
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
style_function = lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))  # won't need to call thsi lambda later, so you can just leave it as a lambda.
# you have to add the read() method. Folium now takes a string instaed of a file as data input.
# POP2005 is a value of the dictionary key 'proprties' in the JSON file.
# 'x' represents 'properties' within 'features' (also in the JSON file)

# this helps you keep your code organized when you want to add other layers; need to add this layer first before Layer Control!!
map.add_child(fgv)
map.add_child(fgp)

# to layers on and off:
map.add_child(folium.LayerControl())

map.save("Map3.html")
