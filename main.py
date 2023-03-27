import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import streamlit.components.v1 as components
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

# initialising and defining dash
app = dash.Dash(__name__)
app.layout = html.Div()

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="@", page_title="Visualizing NSE")
# set_page_config => https://github.com/streamlit/streamlit/issues/1770

# load the available data and overview
df = pd.read_csv("data/data.csv", index_col=0, parse_dates=True)

# sidebar
st.sidebar.header("Nairobi Securities Exchange Stock Prices")
data = st.sidebar.file_uploader("Upload Datase", type=["csv"])


menu = ["Ticker", "Company", "Price", "Date"]
selection = st.sidebar.selectbox("Key Performance Indicator", menu)
if selection =="Ticker":
    st.subheader("Display data")
    st.dataframe(df.head())


dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
figure=px.line(df,
                         x="date",
                         y="price",
                         color="company",
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )