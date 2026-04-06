import streamlit as st
from salaries.utils.helpers import get_salaries_df

df = get_salaries_df()


def job_title_filter():
    return st.selectbox(label="choose your role", options=df["job_title"].unique())


def experience_level_filter():
    return st.selectbox(
        label="choose experience level", options=df["experience_level"].unique()
    )
