import pandas as pd

orders = pd.read_csv(
    "../data/orders.csv"
)

daily_sales = (
    orders.groupby(
        orders["order_date"]
        .str[:10]
    )
    ["order_value"]
    .sum()
    .reset_index()
)

daily_sales.columns = [
    "date",
    "revenue"
]

daily_sales.to_csv(
    "../exports/daily_sales.csv",
    index=False
)

print(
    "Dashboard exports created"
)