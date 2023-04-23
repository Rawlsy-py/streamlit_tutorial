import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime

# Title for Dashboard
st.title('Uber Data Dashboard')

# Dataframe
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Function to load dataset into dataframe
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    timestamp = datetime.datetime.now()
    timestamp = str(timestamp)
    return data, timestamp


# setting load state
data_load_state = st.text('Loading data...')

# load 10,0000 rows of data
data, timestamp = load_data(1000)

# update state when load sucessful
data_load_state.text('Completed')
st.text(f'Data last refreshed at {timestamp}')

