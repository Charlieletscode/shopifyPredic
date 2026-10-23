import pandas as pd
from datetime import timedelta
from collections import defaultdict

# --- Configuration ---
DATA_FILE = 'sales_data.csv'
TARGET_SKU = 'SKU-A101'
FORECAST_DAYS = 7

def load_data(file_path):
    """Loads sales data from CSV."""
    try:
        df = pd.read_csv(file_path)
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        print(f"✅ Successfully loaded {len(df)} records from {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ ERROR: Data file not found at {file_path}. Cannot run prediction.")
        return None

def simple_moving_average(df, sku, window=3):
    """
    Calculates the average quantity sold for a given SKU over the last 'window' days.
    This serves as our basic demonstration of a predictive algorithm.
    """
    sku_data = df[df['product_sku'] == sku].sort_values(by='sale_date')

    if sku_data.empty:
        print(f"❌ No data found for SKU: {sku}")
        return None

    # For demonstration, we'll calculate the rolling average of sales quantity
    sku_data['rolling_avg'] = sku_data['quantity_sold'].rolling(window=window, min_periods=1).mean()
    
    # The most recent calculated average will serve as our short-term forecast baseline
    latest_avg = sku_data['rolling_avg'].iloc[-1]
    print(f"📈 Last recorded rolling average for {sku} (Window={window}): {latest_avg:.2f} units.")
    return latest_avg

def generate_forecast(baseline_avg):
    """
    Generates a simple forecast based on the baseline average.
    For a showcase, we assume a constant average sale rate.
    """
    if baseline_avg is None:
        return None
        
    # Simple projection: baseline_avg per day * number of days
    total_forecast = baseline_avg * FORECAST_DAYS
    print(f"\n🔮 Forecast Generated:")
    print(f"   Based on baseline {baseline_avg:.2f} units/day, the projected sales for the next {FORECAST_DAYS} days is: {total_forecast:.0f} units.")
    return total_forecast

def run_prediction(df):
    """
    Runs the full prediction cycle (SMA Baseline) and returns the forecast.
    """
    average_quantity = simple_moving_average(df, TARGET_SKU, window=3)
    return generate_forecast(average_quantity)

def main():
    # This function remains for script-based execution but calls the exposed function
    sales_df = load_data(DATA_FILE)
    if sales_df is not None:
        forecast = run_prediction(sales_df)
        if forecast:
            print(f"\n🔮 Final Forecast Result: {forecast:.0f} units for the next {FORECAST_DAYS} days.")
        else:
            print("❌ Prediction failed due to data error.")

if __name__ == "__main__":
    main()