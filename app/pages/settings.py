import streamlit as st


def show_settings():
    st.title("Settings")
    st.write("Configure dashboard filters, refresh intervals, and user preferences.")
    if st.button("Reload data"):
        st.rerun()
    st.checkbox("Show advanced analytics", value=False)
    st.selectbox("Default report", ["Overview", "Spend Analysis", "Supplier Insights"])
