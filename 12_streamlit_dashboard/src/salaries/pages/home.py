import streamlit as st
from salaries.utils.helpers import read_textfile
from salaries.utils.constants import MARKDOWN_PATH, IMAGE_PATH

def home():

    st.markdown("# Data salaries insights")
    st.image(IMAGE_PATH / "salaries_data_engineers.png")
    st.markdown(read_textfile(MARKDOWN_PATH / "intro_salaries.md"))

if __name__ == "__main__":
    home()