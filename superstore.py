import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.set_page_config (page_title="SuperStore", layout="wide")


st.title("SuperStore App")



with st.expander("About this app"):
    data = pd.read_excel("sample_superstore.xls")


    st.write(data)

st.title("Super Data Analysis Dasshboard")

st.header("Key Business Metrics")
total_sales = df["Sales"].sum()
total_profit = df