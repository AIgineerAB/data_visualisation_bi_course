import streamlit as st
from salaries.utils.helpers import get_salaries_df
import duckdb

df = get_salaries_df()

df_top_avg_salaries = duckdb.sql("""--sql
    SELECT 
        job_title,
        ROUND(AVG(salary_in_usd),-3)::INT AS avg_salary_usd
    FROM df 
    GROUP BY job_title
    ORDER BY job_title DESC
""").df()


def top_avg_salaries_chart(number_roles=5):
    with st.container(border=True):
        st.markdown("**Top average yearly salary in usd**")
        st.bar_chart(
            df_top_avg_salaries.head(number_roles),
            x="job_title",
            y="avg_salary_usd",
            x_label="JOB TITLE",
            y_label="AVERAGE SALARY USD",
            sort="-avg_salary_usd",
            horizontal=True,
        )


def count_table_chart(feature, label=""):
    dff = df[feature].value_counts()
    st.dataframe(dff)


def filtered_table(job_title, experience_level):
    dff = df.query("job_title == @job_title and experience_level == @experience_level")

    st.markdown(
        f"Average annual salary **${int(round(dff['salary_in_usd'].mean(), -3))}** for {job_title}"
    )
    st.dataframe(dff)
