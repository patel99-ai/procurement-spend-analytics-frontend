import streamlit as st
from components.charts import (
    spend_by_category_bar,
    spend_trend_line,
    category_donut,
    top_suppliers_bar,
    savings_grouped_bar,
)


def show_spend_overview():
    st.title("Spend Overview")
    st.markdown(
        "A consolidated view of procurement spend across categories, suppliers, and time."
    )

    # --- KPI row ---------------------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Spend (YTD)", "$1.25M", "+8.3% vs LY")
    col2.metric("Budget Utilisation", "87%", "-5pp vs target")
    col3.metric("Active Suppliers", "42", "+3 this quarter")
    col4.metric("Realised Savings", "$167K", "+12% vs LY")

    st.divider()

    # --- Trend + Donut ---------------------------------------------------------
    st.subheader("Spend Trend & Distribution")
    left, right = st.columns([3, 2])
    with left:
        st.plotly_chart(spend_trend_line(), use_container_width=True)
    with right:
        st.plotly_chart(category_donut(), use_container_width=True)

    # --- Category breakdown ----------------------------------------------------
    st.subheader("Spend by Category")
    st.plotly_chart(spend_by_category_bar(), use_container_width=True)

    # --- Suppliers + Savings ---------------------------------------------------
    st.subheader("Supplier & Savings Insights")
    sup_col, sav_col = st.columns(2)
    with sup_col:
        st.plotly_chart(top_suppliers_bar(), use_container_width=True)
    with sav_col:
        st.plotly_chart(savings_grouped_bar(), use_container_width=True)

    st.divider()
    st.caption(
        "Data shown is sample/placeholder. Connect a live data source in components/charts.py "
        "to replace the built-in mock datasets."
    )
