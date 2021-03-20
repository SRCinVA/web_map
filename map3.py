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
#      retturn 'red'



map = folium.Map(location=[33.99,-77.5], zoom_start=6, tiles = "Stamen Terrain")

# another way to add children is a feature group
fg = folium.FeatureGroup(name="My Map")

# we can add objects to that map. Multiple markers require multiple methods, or you can use a for loop:
# for coordinates in [[33.98, -77.6], [35.00, -77.6]]:
#   map.add_child(folium.Marker(location = coordinates, popup = "Greetings! I'm a marker.", icon=folium.Icon(color ="green")))

# the zip function lets you iterate over items from multiple separate lists
for lt,ln,el in zip(lat,lon,elev): # strangely, never got his type error; folium had trouble with floats for my code.
    map.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " m", # need to pass <el> to color_producer()
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))
    # he took away 'folium.Icon' -- maybe that was a standard icon of some sort?
    # color = "grey" is for the outline of the dot.
    # nice that you can add radius to the dot.

map.add_child(fg) # this helps you keep your code organized when you want to add other layers

map.save("Map3.html")
