import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv(
    "../data/orders.csv"
)

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

monthly = (
    orders.groupby(
        orders["order_date"]
        .dt.to_period("M")
    )
    ["order_value"]
    .sum()
)

plt.figure(
    figsize=(10,5)
)

monthly.plot()

plt.title(
    "Monthly Revenue Trend"
)

plt.tight_layout()

plt.savefig(
    "../exports/revenue_trend.png"
)

print(
    "Revenue chart saved"
)