import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()

os.makedirs("../data", exist_ok=True)

# --------------------------
# Customers
# --------------------------

cities = [
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Mumbai",
    "Pune"
]

customers = []

for i in range(1, 5001):

    customers.append([
        i,
        fake.name(),
        random.choice(cities),
        fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    ])

customers_df = pd.DataFrame(
    customers,
    columns=[
        "customer_id",
        "customer_name",
        "city",
        "signup_date"
    ]
)

# --------------------------
# Products
# --------------------------

categories = {
    "Fruits":["Apple","Banana","Orange","Mango"],
    "Vegetables":["Tomato","Potato","Onion","Carrot"],
    "Beverages":["Coke","Pepsi","Sprite","Juice"],
    "Snacks":["Chips","Cookies","Namkeen","Biscuits"],
    "Dairy":["Milk","Cheese","Butter","Curd"]
}

products = []

product_id = 1

for category, items in categories.items():

    for item in items:

        products.append([
            product_id,
            item,
            category,
            round(
                random.uniform(20,500),
                2
            )
        ])

        product_id += 1

products_df = pd.DataFrame(
    products,
    columns=[
        "product_id",
        "product_name",
        "category",
        "price"
    ]
)

# --------------------------
# Orders
# --------------------------

orders = []

for order_id in range(1, 50001):

    customer_id = random.randint(
        1,
        5000
    )

    order_date = datetime.now() - timedelta(
        days=random.randint(0,365)
    )

    order_value = round(
        random.uniform(100,3000),
        2
    )

    orders.append([
        order_id,
        customer_id,
        order_date,
        order_value
    ])

orders_df = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "customer_id",
        "order_date",
        "order_value"
    ]
)

# --------------------------
# Order Items
# --------------------------

order_items = []

order_item_id = 1

for order_id in range(1,50001):

    item_count = random.randint(1,5)

    chosen_products = random.sample(
        list(products_df["product_id"]),
        item_count
    )

    for pid in chosen_products:

        order_items.append([
            order_item_id,
            order_id,
            pid,
            random.randint(1,5)
        ])

        order_item_id += 1

order_items_df = pd.DataFrame(
    order_items,
    columns=[
        "order_item_id",
        "order_id",
        "product_id",
        "quantity"
    ]
)

# --------------------------
# Export CSV
# --------------------------

customers_df.to_csv(
    "../data/customers.csv",
    index=False
)

products_df.to_csv(
    "../data/products.csv",
    index=False
)

orders_df.to_csv(
    "../data/orders.csv",
    index=False
)

order_items_df.to_csv(
    "../data/order_items.csv",
    index=False
)

print("Data Generated Successfully")

print("Customers:", len(customers_df))
print("Products:", len(products_df))
print("Orders:", len(orders_df))
print("Order Items:", len(order_items_df))