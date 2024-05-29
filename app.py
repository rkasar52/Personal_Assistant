import streamlit as st
import pandas as pd
import numpy as np


# col1, col2 = st.columns(2)

df = pd.read_excel('./Master_List.xlsx', sheet_name='Bathroom')
df['With_Me'] = False
item_list = df['Item'].unique()
location_list = df['Location'].unique()





selected_items = st.sidebar.multiselect(
    "Select an item",
    item_list)

selected_location = st.sidebar.selectbox(
    "Select a Storage Unit",
    location_list, index = None)
    



if selected_location and not selected_items:
    # Filter to the selected storage unit
    df_display = df[df['Location'] == selected_location]

    items_in_unit = df_display.shape[0]

elif selected_items and not selected_location:
    df_display = df[df['Item'].isin(selected_items)]
elif selected_location and selected_items:
    df_display = df[(df['Location'] == selected_location) & (df['Item'].isin(selected_items))]


else:
    df_display = df


edited_df = st.data_editor(df_display[['Item', 'Location', 'Health', 'With_Me']], num_rows="dynamic", key = 'my_data_editor')



