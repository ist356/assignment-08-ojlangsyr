import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    violations_df = violations_df.groupby('location').agg({'amount': 'sum'}).reset_index()
    return violations_df[violations_df['amount'] >= threshold]


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locations_df = top_locations(violations_df, threshold)
    violations_merge = violations_df[['location', 'lat', 'lon']].drop_duplicates(subset=['location'])
    return pd.merge(top_locations_df, violations_merge, on='location').drop_duplicates()

def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locations_df = top_locations(violations_df, threshold)
    return pd.merge(top_locations_df[['location']], violations_df, on='location')

if __name__ == '__main__':
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    top_locations_df = top_locations(violations_df)
    top_locations_df.to_csv('./cache/top_locations.csv', index=False)
    top_locations_mappable_df = top_locations_mappable(violations_df)
    top_locations_mappable_df.to_csv('./cache/top_locations_mappable.csv', index=False)
    tickets_in_top_locations_df = tickets_in_top_locations(violations_df)
    tickets_in_top_locations_df.to_csv('./cache/tickets_in_top_locations.csv', index=False)