'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
st.set_page_config(layout="wide")


st.title('Location Dashboard')

top_locations_df = pd.read_csv('./cache/top_locations.csv')
top_locations_mappable_df = pd.read_csv('./cache/top_locations_mappable.csv')
tickets_in_top_locations_df = pd.read_csv('./cache/tickets_in_top_locations.csv')

st.write('Top Locations')
st.write(top_locations_df)


map = folium.map(location=[43.03986, -76.13375], zoom_start=13)
