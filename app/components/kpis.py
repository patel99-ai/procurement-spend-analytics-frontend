"""KPI cards for procurement spend analytics dashboard."""

from typing import Optional
import streamlit as st


def display_total_spend_kpi(total_spend: float, delta: Optional[float] = None, currency: str = "$"):
    """
    Display total spend KPI card.
    
    Args:
        total_spend (float): The total spend amount.
        delta (float, optional): The change from previous period. Defaults to None.
        currency (str): Currency symbol to display. Defaults to "$".
    """
    formatted_spend = f"{currency}{total_spend:,.2f}"
    if delta is not None:
        delta_str = f"{delta:+.2f}%" if delta >= 0 else f"{delta:.2f}%"
    else:
        delta_str = None
    
    st.metric(
        label="Total Spend",
        value=formatted_spend,
        delta=delta_str,
        help="Total procurement spend across all categories"
    )


def display_supplier_count_kpi(supplier_count: int, delta: Optional[int] = None):
    """
    Display supplier count KPI card.
    
    Args:
        supplier_count (int): The total number of suppliers.
        delta (int, optional): The change in supplier count from previous period. Defaults to None.
    """
    delta_str = f"{delta:+d}" if delta is not None else None
    
    st.metric(
        label="Supplier Count",
        value=supplier_count,
        delta=delta_str,
        help="Total number of active suppliers"
    )


def display_kpi_row(total_spend: float, supplier_count: int, spend_delta: Optional[float] = None, supplier_delta: Optional[int] = None):
    """
    Display KPI cards in a row layout.
    
    Args:
        total_spend (float): The total spend amount.
        supplier_count (int): The total number of suppliers.
        spend_delta (float, optional): The spend change percentage. Defaults to None.
        supplier_delta (int, optional): The supplier count change. Defaults to None.
    """
    col1, col2 = st.columns(2)
    
    with col1:
        display_total_spend_kpi(total_spend, delta=spend_delta)
    
    with col2:
        display_supplier_count_kpi(supplier_count, delta=supplier_delta)


def display_kpi_grid(total_spend: float, supplier_count: int, spend_delta: Optional[float] = None, supplier_delta: Optional[int] = None):
    """
    Display KPI cards in a flexible grid layout with more visual appeal.
    
    Args:
        total_spend (float): The total spend amount.
        supplier_count (int): The total number of suppliers.
        spend_delta (float, optional): The spend change percentage. Defaults to None.
        supplier_delta (int, optional): The supplier count change. Defaults to None.
    """
    col1, col2 = st.columns([1, 1], gap="medium")
    
    with col1:
        st.metric(
            label="💰 Total Spend",
            value=f"${total_spend:,.2f}",
            delta=f"{spend_delta:+.2f}%" if spend_delta is not None else None,
            help="Total procurement spend across all categories and time periods"
        )
    
    with col2:
        st.metric(
            label="🤝 Supplier Count",
            value=supplier_count,
            delta=f"{supplier_delta:+d}" if supplier_delta is not None else None,
            help="Total number of active suppliers in the system"
        )
