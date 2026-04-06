import streamlit as st 

pages = [
    st.Page("pages/home.py", title = "Home"),
    st.Page("pages/dashboard.py", title = "Dashboard"),
    st.Page("pages/raw_data.py", title = "Raw Data"),
]

pg = st.navigation(pages)

pg.run()