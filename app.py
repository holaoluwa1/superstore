import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first streamlit app.")


name = st.text_input("Enter your name:")
st.write(f"Hello,{name}")
checkbox = st.checkbox("Show greeting")
radio = st.radio("Choose a greeting style:", ("formal","Casual"))
date = st.date_input("select a date")
color = st.color_picker("Pick a color:", "#00f900")
image = st.file_uploader("Upload an image:", type = ["png", "jpg","jpeg"])
select = st.select_slider("select", ("Formal","Casual","Native"))
image = st.image("c:\\Users\\USER\Downloads\\bg-header-sqi-1-removebg-preview.png")
video = st.video("c:\\Users\\USER\\Downloads\\videoplayback.mp4")

st.sidebar.title("Side Menu")
st.sidebar.text_input("Enter Your Name:")
st.sidebar.write(f"My name is {name}")