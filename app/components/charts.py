"""Reusable Plotly chart builders for procurement spend analytics."""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# ---------------------------------------------------------------------------
# Sample / mock data helpers
# ---------------------------------------------------------------------------

def _sample_spend_by_category() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Category": [
                "IT & Software",
                "Facilities",
                "Marketing",
                "Logistics",
                "HR & Staffing",
                "Professional Services",
                "Raw Materials",
            ],
            "Spend ($K)": [320, 215, 180, 145, 110, 95, 185],
        }
    )


def _sample_spend_trend() -> pd.DataFrame:
    months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    ]
    spend = [95, 102, 88, 115, 130, 120, 105, 140, 132, 118, 145, 160]
    budget = [110, 110, 110, 120, 120, 120, 130, 130, 130, 140, 140, 140]
    return pd.DataFrame({"Month": months, "Actual Spend ($K)": spend, "Budget ($K)": budget})


def _sample_supplier_spend() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Supplier": [
                "Acme Corp",
                "GlobalTech",
                "SupplyBase Inc",
                "NovaParts",
                "Zenith Logistics",
                "BridgeCo",
                "Apex Solutions",
                "CoreLink",
            ],
            "Spend ($K)": [285, 210, 178, 145, 132, 98, 87, 65],
        }
    )


def _sample_savings() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Quarter": ["Q1", "Q2", "Q3", "Q4"],
            "Identified ($K)": [42, 55, 48, 63],
            "Realized ($K)": [30, 44, 38, 55],
        }
    )


# ---------------------------------------------------------------------------
# Chart builders
# ---------------------------------------------------------------------------

def spend_by_category_bar(df: pd.DataFrame | None = None) -> go.Figure:
    """Horizontal bar chart — spend by procurement category."""
    if df is None:
        df = _sample_spend_by_category()

    df = df.sort_values("Spend ($K)", ascending=True)
    fig = px.bar(
        df,
        x="Spend ($K)",
        y="Category",
        orientation="h",
        color="Spend ($K)",
        color_continuous_scale="Blues",
        text="Spend ($K)",
        title="Spend by Category",
    )
    fig.update_traces(texttemplate="$%{text}K", textposition="outside")
    fig.update_layout(
        coloraxis_showscale=False,
        margin=dict(l=10, r=30, t=50, b=10),
        height=380,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
        yaxis=dict(showgrid=False),
    )
    return fig


def spend_trend_line(df: pd.DataFrame | None = None) -> go.Figure:
    """Line chart — monthly actual spend vs budget."""
    if df is None:
        df = _sample_spend_trend()

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Actual Spend ($K)"],
            mode="lines+markers",
            name="Actual Spend",
            line=dict(color="#1f77b4", width=2.5),
            marker=dict(size=7),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Budget ($K)"],
            mode="lines",
            name="Budget",
            line=dict(color="#ff7f0e", width=2, dash="dash"),
        )
    )
    fig.update_layout(
        title="Monthly Spend vs Budget",
        xaxis_title="Month",
        yaxis_title="$K",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=10, r=10, t=55, b=10),
        height=340,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
    )
    return fig


def category_donut(df: pd.DataFrame | None = None) -> go.Figure:
    """Donut chart — proportional spend share per category."""
    if df is None:
        df = _sample_spend_by_category()

    fig = px.pie(
        df,
        names="Category",
        values="Spend ($K)",
        hole=0.45,
        title="Spend Distribution",
        color_discrete_sequence=px.colors.sequential.Blues_r,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(
        margin=dict(l=10, r=10, t=55, b=10),
        height=370,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def top_suppliers_bar(df: pd.DataFrame | None = None) -> go.Figure:
    """Bar chart — top suppliers by spend."""
    if df is None:
        df = _sample_supplier_spend()

    df = df.sort_values("Spend ($K)", ascending=False).head(8)
    fig = px.bar(
        df,
        x="Supplier",
        y="Spend ($K)",
        color="Spend ($K)",
        color_continuous_scale="Teal",
        text="Spend ($K)",
        title="Top Suppliers by Spend",
    )
    fig.update_traces(texttemplate="$%{text}K", textposition="outside")
    fig.update_layout(
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=55, b=10),
        height=370,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, tickangle=-30),
        yaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
    )
    return fig


def savings_grouped_bar(df: pd.DataFrame | None = None) -> go.Figure:
    """Grouped bar chart — identified vs realised savings per quarter."""
    if df is None:
        df = _sample_savings()

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df["Quarter"],
            y=df["Identified ($K)"],
            name="Identified",
            marker_color="#4C72B0",
            text=df["Identified ($K)"],
            texttemplate="$%{text}K",
            textposition="outside",
        )
    )
    fig.add_trace(
        go.Bar(
            x=df["Quarter"],
            y=df["Realized ($K)"],
            name="Realized",
            marker_color="#55A868",
            text=df["Realized ($K)"],
            texttemplate="$%{text}K",
            textposition="outside",
        )
    )
    fig.update_layout(
        barmode="group",
        title="Savings: Identified vs Realized",
        yaxis_title="$K",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=10, r=10, t=55, b=10),
        height=340,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
    )
    return fig
