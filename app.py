import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from worker_details import show_team_details


page = st.sidebar.selectbox("Explore, Predict or About Us", ("Predict", "Explore", "About Us"))

if page == "Predict":
    show_predict_page()
elif page == "About Us":
    show_team_details()
else:
    show_explore_page()
