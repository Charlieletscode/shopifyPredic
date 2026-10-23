# app.py
import streamlit as st
import pandas as pd
import numpy as np
from predict_inventory import run_prediction

st.set_page_config(page_title="Shopify Inventory Forecasting Showcase", layout="wide")

def load_data():
    """Loads and displays the sales data."""
    try:
        df = pd.read_csv("sales_data.csv")
        return df
    except FileNotFoundError:
        st.error("Error: sales_data.csv not found in src/ directory.")
        return pd.DataFrame()

def run_forecast(df):
    """Runs the prediction model (SMA baseline)."""
    # In a real implementation, this would call the core logic from predict_inventory.py
    # For this demo, we simulate running the prediction on the loaded data.
    if not df.empty:
        st.info("Running prediction (SMA Baseline)...")
        # Simulate prediction output
        forecast = df['quantity_sold'].rolling(window=3).mean().rename('SMA_Forecast')
        return forecast
    return pd.Series()

st.title("📦 Shopify Predictive Inventory Forecasting Showcase")
st.markdown("---")

# 1. Data Input/Display
sales_df = load_data()
if not sales_df.empty:
    st.header("📊 Historical Sales Data")
    st.dataframe(sales_df)

    # 2. Run Prediction
    forecast_series = run_forecast(sales_df)

    if not forecast_series.empty:
        st.header("📈 Demand Forecast Output")
        st.line_chart(forecast_series)
        st.success("✅ Prediction successfully generated based on SMA baseline.")
    else:
        st.warning("Cannot generate forecast. Check data integrity.")
else:
    st.error("❌ Project setup incomplete. Data file not found.")