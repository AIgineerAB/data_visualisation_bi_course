import streamlit as st
from salaries.utils.helpers import get_salaries_df
import duckdb

df = get_salaries_df()


def average_salary_usd_kpi(role=None, label=""):
    avg_salary = duckdb.sql(f"""--sql
        SELECT 
            ROUND(AVG(salary_in_usd),-3)::INT AS avg_salary_usd
        FROM df
        WHERE job_title ILIKE '{role}'
        GROUP BY job_title                                  
    """).df()

    st.metric(label=label, value=f"${avg_salary['avg_salary_usd'].iloc[0]}")
