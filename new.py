import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import plotly.express as px


file_path = "sample_superstore.xls"
df = pd.read_excel(file_path)

st.title("Super Data Analysis Dashboard")
if st.checkbox("Show raw dataset"):
    st.dataframe(df)




st.subheader("Dataset Summary")
st.write(df.describe())



st.subheader("Key Business Metrics")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order id"].nunique()



st.metric("Total Sales," f"#{total_sales}")
st.metric("Total Profit," f"#{total_profit}")
st.metric("Total Order," f"#{total_orders}")



st.subheader("Profit by Category")
category_sales = df.groupby("Category")
["Sales"].sum().reset_index()
st.bar_chart(catagory_sale.set_index("Category"))


st.subheader("Profit by Categoty")
plt.figure()
sns.barplot(x="Catagory", y= "Profit", data=df, estimator=sum)
st.pyplot(plt)

