import streamlit as st


def show_overview():
    st.title("Overview")
    st.metric(label="Total Spend", value="$1.25M")
    st.metric(label="Supplier Count", value="42")
    st.metric(label="Savings Opportunity", value="$128K")
    st.divider()
    st.write(
        "This overview provides a quick summary of procurement spend across categories and supplier performance."
    )
    st.info(
        "Add charts, tables, or KPIs here to visualize spend trends, top categories, and savings opportunities."
    )
