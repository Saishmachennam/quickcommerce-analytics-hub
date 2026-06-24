import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:"
    "password@localhost:5432/"
    "quickcommerce"
)

engine = create_engine(
    DATABASE_URL
)

pd.read_csv(
    "../data/customers.csv"
).to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "../data/products.csv"
).to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "../data/orders.csv"
).to_sql(
    "orders",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "../data/order_items.csv"
).to_sql(
    "order_items",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded")