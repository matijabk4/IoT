import folium
import os
import json
m = folium.Map(location=[44.79761313934651, 20.434948293479355], zoom_start=13)
vis = os.path.join('data', 'vis.json')
vis1 = os.path.join('data', 'vis1.json')
vis2 = os.path.join('data', 'vis2.json')
vis3 = os.path.join('data', 'vis3.json')
vis4 = os.path.join('data', 'vis4.json')
vis5 = os.path.join('data', 'vis5.json')
vis6 = os.path.join('data', 'vis6.json')
vis7 = os.path.join('data', 'vis7.json')
vis8 = os.path.join('data', 'vis8.json')
vis9 = os.path.join('data', 'vis9.json')

overlay = os.path.join('data', 'overlay.json')


folium.Marker([44.78964787826317, 20.4664977583781],
            tooltip='Autokomanda',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='red'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis9)), width=450, height=280))).add_to(m),
folium.Marker([44.75617744172545, 20.4769512336477],
            tooltip='Banjica',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='blue'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis8)), width=450, height=280))).add_to(m),
folium.Marker([44.768087391424814, 20.49229493597008],
            tooltip='Brace Jerkovic',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='green'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis7)), width=450, height=280))).add_to(m),
folium.Marker([44.8157349019317, 20.491060018369023],
            tooltip='Bogoslovija',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='purple'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis6)), width=450, height=280))).add_to(m),
folium.Marker([44.802243322526095, 20.46631430598974],
            tooltip='Slavija',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='orange'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis5)), width=450, height=280))).add_to(m),
folium.Marker([44.82132164512155, 20.468377394870913],
            tooltip='Zorza Klemansoa',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='darkgreen'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis4)), width=450, height=280))).add_to(m),
folium.Marker([44.801864009602866, 20.386446687951928],
            tooltip='TC Piramida',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='darkblue'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis3)), width=450, height=280))).add_to(m),
folium.Marker([44.83188118015894, 20.40766460335015],
            tooltip='Otona Zupancica',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='cadetblue'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis2)), width=450, height=280))).add_to(m),
folium.Marker([44.826149522263115, 20.402434964573523],
            tooltip='Studentska',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='darkred'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis1)), width=450, height=280))).add_to(m),
folium.Marker([44.81500807239675, 20.47095682266451],
            tooltip='Dzordza Vasingtona',
            icon=folium.Icon(prefix='fa',icon='bus',markerColor='darkpurple'),
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=280))).add_to(m)



folium.GeoJson(overlay, name='Beograd').add_to(m)
m.save('map.html')