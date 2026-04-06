import streamlit as st
from salaries.utils.helpers import read_textfile, read_css
from salaries.utils.constants import MARKDOWN_PATH, STYLE_PATH
from salaries.components.kpis import average_salary_usd_kpi
from salaries.components.visualizations import (
    top_avg_salaries_chart,
    count_table_chart,
    filtered_table,
)
from salaries.components.filters import job_title_filter, experience_level_filter


def dashboard_layout():
    st.markdown("# Salaries dashboard")
    st.markdown(read_textfile(MARKDOWN_PATH / "salaries_dashboard_description.md"))

    st.markdown("**Yearly salaries in USD for some common data roles**")

    roles = (
        "Data engineer",
        "Data scientist",
        "Data analyst",
        "Machine learning engineer",
        "AI engineer",
    )

    cols = st.columns(len(roles))

    for col, role in zip(cols, roles):
        with col:
            average_salary_usd_kpi(role=role, label=role)

    top_avg_salaries_chart(7)

    st.markdown("## Some value counts tables")

    features = ("company_size", "remote_ratio", "salary_currency", "experience_level")
    cols = st.columns(len(features))

    for col, feature in zip(cols, features):
        with col:
            count_table_chart(feature=feature, label=feature)

    st.markdown("## Filters")

    cols = st.columns(3)

    with cols[0]:
        job_title = job_title_filter()
    with cols[1]:
        experience_lvl = experience_level_filter()

    filtered_table(job_title=job_title, experience_level=experience_lvl)

    read_css(STYLE_PATH / "dashboard.css")

if __name__ == "__main__":
    dashboard_layout()
