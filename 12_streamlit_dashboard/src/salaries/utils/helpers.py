from pathlib import PosixPath
import pandas as pd 
import streamlit as st 
from salaries.utils.constants import DATA_PATH

def read_textfile(path: PosixPath) -> str:
    with open(path) as file:
        return file.read()


def read_css(path: PosixPath) -> str:
    css = read_textfile(path)
    st.write(
        f"<style>{css}</style>", unsafe_allow_html=True
    )

@st.cache_data
def get_salaries_df():
    return pd.read_csv(DATA_PATH / "salaries.csv")

