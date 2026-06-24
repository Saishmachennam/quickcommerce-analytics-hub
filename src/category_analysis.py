import pandas as pd

products = pd.read_csv(
    "../data/products.csv"
)

order_items = pd.read_csv(
    "../data/order_items.csv"
)

merged = (
    order_items
    .merge(
        products,
        on="product_id"
    )
)

merged["sales"] = (
    merged["quantity"]
    * merged["price"]
)

category_performance = (
    merged.groupby("category")
    .agg(
        total_sales=("sales","sum"),
        quantity_sold=("quantity","sum")
    )
    .reset_index()
)

category_performance.to_csv(
    "../exports/category_performance.csv",
    index=False
)

print(category_performance)