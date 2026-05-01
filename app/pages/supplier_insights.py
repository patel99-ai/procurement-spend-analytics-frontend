import streamlit as st


def show_supplier_insights():
    st.title("Supplier Insights")
    st.write("Review supplier performance, contract compliance, and risk indicators.")
    st.write("- Top suppliers by spend")
    st.write("- Supplier risk score")
    st.write("- Contract renewal alerts")
    st.success(
        "Use this page to monitor supplier relationships and identify opportunities to consolidate spend."
    )
