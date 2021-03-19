import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[33.99,-77.5], zoom_start=6, tiles = "Stamen Terrain")

# another way to add children is a feature group
fg = folium.FeatureGroup(name="My Map")

# we can add objects to that map. Multiple markers require multiple methods, or you can use a for loop:
# for coordinates in [[33.98, -77.6], [35.00, -77.6]]:
#   map.add_child(folium.Marker(location = coordinates, popup = "Greetings! I'm a marker.", icon=folium.Icon(color ="green")))

# the zip function lets you iterate over items from multiple separate lists
for lt,ln,el in zip(lat,lon,elev): # strangely, never got his type error; folium had trouble with floats for my code.
    map.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " m", icon=folium.Icon(color ="green")))


map.add_child(fg) # this helps you keep your code organized when you want to add other layers

map.save("Map3.html")
