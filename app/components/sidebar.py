import streamlit as st

NAV_OPTIONS = [
    "Overview",
    "Spend Analysis",
    "Supplier Insights",
    "Settings",
]


def render_sidebar() -> str:
    """Render the sidebar navigation and return the selected page name."""
    st.sidebar.title("📊 Procurement Analytics")
    st.sidebar.markdown("---")
    selected = st.sidebar.radio("Navigation", NAV_OPTIONS)
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built for procurement teams to explore spend analytics.")
    return selected
