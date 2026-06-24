import pandas as pd

order_items = pd.read_csv(
    "../data/order_items.csv"
)

basket_size = (
    order_items.groupby(
        "order_id"
    )
    ["quantity"]
    .sum()
)

basket_df = pd.DataFrame({
    "average_basket_size":[
        round(
            basket_size.mean(),
            2
        )
    ]
})

basket_df.to_csv(
    "../exports/basket_analysis.csv",
    index=False
)

print(basket_df)