import folium
map = folium.Map(location=[33.99,-77.5], zoom_start=6, tiles = "Stamen Terrain")
# we can add objects to that map
map.add_child(folium.Marker(location = [33.98,-77.6], popup= "Greetings! I'm a marker.", icon=folium.Icon(color ="green")))

map.save("Map3.html")