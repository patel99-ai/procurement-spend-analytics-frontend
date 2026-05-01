import streamlit as st


def init_ui():
    st.set_page_config(
        page_title="Procurement Spend Analytics",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Procurement Spend Analytics")
    st.markdown(
        "Use the sidebar to navigate between analytics views and supplier insights."
    )
    st.write("This dashboard helps teams monitor spend, suppliers, and budget performance.")


def show_overview():
    st.header("Overview")
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


def show_spend_analysis():
    st.header("Spend Analysis")
    st.write("Analyze spend by category, department, and purchase type.")
    st.subheader("Category breakdown")
    st.write("(Placeholder content — connect your spend dataset here.)")
    st.progress(0.65)
    st.caption("Example: 65% of spend is concentrated in top 3 categories.")


def show_supplier_insights():
    st.header("Supplier Insights")
    st.write("Review supplier performance, contract compliance, and risk indicators.")
    st.write("- Top suppliers by spend")
    st.write("- Supplier risk score")
    st.write("- Contract renewal alerts")
    st.success("Use this page to monitor supplier relationships and identify opportunities to consolidate spend.")


def show_settings():
    st.header("Settings")
    st.write("Configure dashboard filters, refresh intervals, and user preferences.")
    if st.button("Reload data"):
        st.experimental_rerun()
    st.checkbox("Show advanced analytics", value=False)
    st.selectbox("Default report", ["Overview", "Spend Analysis", "Supplier Insights"])


def main():
    init_ui()

    nav_options = [
        "Overview",
        "Spend Analysis",
        "Supplier Insights",
        "Settings",
    ]

    selected_page = st.sidebar.radio("Navigation", nav_options)
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built for procurement teams to explore spend analytics.")

    if selected_page == "Overview":
        show_overview()
    elif selected_page == "Spend Analysis":
        show_spend_analysis()
    elif selected_page == "Supplier Insights":
        show_supplier_insights()
    elif selected_page == "Settings":
        show_settings()


if __name__ == "__main__":
    main()
