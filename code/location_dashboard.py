'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import streamlit_folium as sf

st.set_page_config(layout="wide")


st.title('Location Dashboard')

top_locations_df = pd.read_csv('./cache/top_locations.csv')
top_locations_mappable_df = pd.read_csv('./cache/top_locations_mappable.csv')
tickets_in_top_locations_df = pd.read_csv('./cache/tickets_in_top_locations.csv')

location = st.selectbox('Select Location', top_locations_df['location'].unique())

col1, col2 = st.columns(2)

with col1:
    st.write('Tickets in Top Locations')
    st.write(f'{len(tickets_in_top_locations_df[tickets_in_top_locations_df['location'] == location])}')
    fig2, ax2 = plt.subplots()
    ax2.set_title('Tickets Issued by Hour of Day')
    sns.barplot(data=tickets_in_top_locations_df[tickets_in_top_locations_df['location'] == location], x='hourofday', y='count', estimator='sum', hue='hourofday', ax=ax2)
    st.pyplot(fig2)
with col2:
    st.write('Total Amount')
    st.write(f'{top_locations_df[top_locations_df['location'] == location]['amount'].values[0]}')
    fig1, ax1 = plt.subplots()
    ax1.set_title('Tickets Issued by Day of Week')
    sns.barplot(data=tickets_in_top_locations_df[tickets_in_top_locations_df['location'] == location], x='dayofweek', y='count', estimator='sum', hue='dayofweek', ax=ax1)
    st.pyplot(fig1)


#st.map of selected input
st.map(top_locations_mappable_df[top_locations_mappable_df['location'] == location][['lat', 'lon']])
