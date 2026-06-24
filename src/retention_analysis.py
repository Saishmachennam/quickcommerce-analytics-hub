import pandas as pd

orders = pd.read_csv(
    "../data/orders.csv"
)

customer_orders = (
    orders.groupby(
        "customer_id"
    )
    .size()
    .reset_index(name="orders")
)

repeat_customers = (
    customer_orders[
        customer_orders["orders"] > 1
    ]
)

repeat_rate = round(
(
len(repeat_customers)
/
len(customer_orders)
)*100,
2
)

retention = pd.DataFrame({
    "metric":[
        "Total Customers",
        "Repeat Customers",
        "Repeat Purchase Rate"
    ],
    "value":[
        len(customer_orders),
        len(repeat_customers),
        repeat_rate
    ]
})

retention.to_csv(
    "../exports/retention_metrics.csv",
    index=False
)

print(retention)