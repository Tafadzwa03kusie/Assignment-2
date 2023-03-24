import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import streamlit.components.v1 as components
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="@", page_title="Visualizing NSE")
# set_page_config => https://github.com/streamlit/streamlit/issues/1770

# load the available data and overview
path = "./data/data.csv"

# sidebar
st.sidebar.header("Nairobi Securities Exchange Stock Prices")
data = st.sidebar.file_uploader("Upload Datase", type=["csv"])


menu = ["Ticker", "Company", "Price", "Date"]
selection = st.sidebar.selectbox("Key Performance Indicator", menu)
if selection =="Ticker":
    st.subheader("Display data")
    st. dataframe(df.head())