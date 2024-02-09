import folium
import webbrowser

# Create a map
m = folium.Map(location=[45.5236, -122.6750])

icon = folium.Icon(color="red")

# Add a marker at the exact location
folium.Marker([45.5236, -122.6750], popup='Marker Location', icon=icon).add_to(m)

# Save it to html
m.save('map.html')

# Open the web page in the default browser
webbrowser.open_new_tab('map.html')
