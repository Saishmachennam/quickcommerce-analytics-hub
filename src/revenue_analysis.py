import pandas as pd
import os

os.makedirs("../exports", exist_ok=True)

orders = pd.read_csv("../data/orders.csv")

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

orders["month"] = (
    orders["order_date"]
    .dt.to_period("M")
)

monthly_revenue = (
    orders.groupby("month")
    ["order_value"]
    .sum()
    .reset_index()
)

monthly_revenue.columns = [
    "month",
    "revenue"
]

monthly_revenue.to_csv(
    "../exports/revenue_summary.csv",
    index=False
)

print(monthly_revenue.tail())