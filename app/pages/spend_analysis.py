import streamlit as st


def show_spend_analysis():
    st.title("Spend Analysis")
    st.write("Analyze spend by category, department, and purchase type.")
    st.subheader("Category Breakdown")
    st.write("(Placeholder — connect your spend dataset here.)")
    st.progress(0.65)
    st.caption("Example: 65% of spend is concentrated in top 3 categories.")
