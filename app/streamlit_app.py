import streamlit as st
from components.sidebar import render_sidebar

# Page imports
from pages.overview import show_overview
from pages.Spend_Overview import show_spend_overview
from pages.spend_analysis import show_spend_analysis
import pages.supplier_insights
from pages.settings import show_settings


def init_ui():
    st.set_page_config(
        page_title="Procurement Spend Analytics",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def main():
    init_ui()
    selected_page = render_sidebar()

    if selected_page == "Overview":
        show_overview()
    elif selected_page == "Spend Overview":
        show_spend_overview()
    elif selected_page == "Spend Analysis":
        show_spend_analysis()
    elif selected_page == "Supplier Insights":
        pages.supplier_insights.show_supplier_insights()
    elif selected_page == "Settings":
        show_settings()


if __name__ == "__main__":
    main()
