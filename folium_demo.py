# -*- coding: utf-8 -*-

import time
import folium

for x in xrange(0,10):
    #
    Yonaguni = folium.Map(location=[24.454684, 122.983647], zoom_start=12)
    
    # Polygon markers
    Yonaguni.polygon_marker(location=[24.467419+0.003*x, 122.980649+0.003*x], 
                            popup='num_sides=3', fill_color='#132b5e', num_sides=3, radius=10)
    Yonaguni.polygon_marker(location=[24.451+0.003*x, 122.961+0.003*x], 
                            popup='num_sides=4', fill_color='#45647d', num_sides=4, radius=10)
    Yonaguni.polygon_marker(location=[24.452+0.003*x, 122.972+0.003*x], 
                            popup='num_sides=6', fill_color='#769d96', num_sides=6, radius=10)
    Yonaguni.polygon_marker(location=[24.453+0.003*x, 122.983+0.003*x], 
                            popup='num_sides=8', fill_color='#769d96', num_sides=8, radius=10)
    #
    Yonaguni.create_map(path='Yonaguni.html')
    #
    time.sleep(6)
    
    