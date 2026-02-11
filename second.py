import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config (page_title="Data Viz App", layout="wide")

st.title("Data vizualization App")


with st.expander("About this app"):
    data = pd.read_csv("train.csv")

    #data = st.file_uploader("Upload your CVS file", type=["cvs"])

    #if data is not None:
    #data = pd.read_cvs(data)

    st.write(data)


left_column, right_column = st.columns(2)


with left_column:
    st.header("Data Table")
    st.dataframe(data)


    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"]) 

    with tab1:
        st.subheader("Gender Analysis")
        gender = data['Sex'].value_counts()
        #st.data_editor(gender)
        st.dataframe(gender)   
        #st.bar_chart(gender)


    with tab2:
        st.subheader("Age Analysis")  
        age_tab1, age_tab2 = st.tabs(["Age Stats", "Age Chart"])
        with age_tab1:
            age = data["Age"].describe()
            st.dataframe(age)
        with tab2:
            st.markdown("### Gender with the Higest Age") 
            age_gender = data.groupby('Sex')['Age'].mean() 
            st.write(age_gender)

        with tab3:
            st.markdown("### Gender by the Survived Distribution")
            #data["DeadorALive"] = data["Survived"].map({0: "Non-survived", 1: "Survived"})
           # data["DeadorALive"] = np.where(data["Survived"]==1 "Survived", "Non-survived")
            survived_gender = pd.pivot_table(data, index="Sex", columns="Survived", values="PassengerId", aggfunc="count")
            st.dataframe(survived_gender)


with right_column:
    st.header("Data Visualization")
    st.subheader("Passenger Class Distribution")
    pclass = data["Pclass"].value_counts()
    st.bar_chart(pclass)


    tab_rig, tab_rig2 = st.tabs(["Survival Status", "Age Distribution"])
    st.subheader("Age Distribution")
    with tab_rig:
        st.subheader("Survival Status Distribution")
        survived = data["Survived"].value_counts()


    with tab_rig2:
        st.subheader("Age Distribution Histogram")
        fig = px.histogram(data["Age"].dropna(), nbins = 30, title= "Distribution of Age")
        st.plotly_chart(fig, theme="streamlit")                