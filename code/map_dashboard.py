'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd
# these constants should help you get the map to look better
# you need to figure out where to use them
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale

st.title('Map Dashboard')
toplocdf = pd.read_csv('./cache/top_locations_mappable.csv')
gdf = gpd.GeoDataFrame(toplocdf, geometry=gpd.points_from_xy(toplocdf.lon, toplocdf.lat))

m = folium.Map(location=CUSE, zoom_start=ZOOM)
map = gdf.explore(gdf['amount'],
                   m = m,
                   vmin = VMIN,
                   vmax = VMAX,
                   market_type = 'circleMarker',
                   fill = True)
st.write(f"Number of locations where tickets exceed $1000: {len(toplocdf)}")
sf.folium_static(map)

