from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="QuickCommerce Analytics API"
)

@app.get("/")
def home():
    return {
        "message":
        "QuickCommerce Analytics Hub"
    }

@app.get("/revenue")
def revenue():

    df = pd.read_csv(
        "../exports/revenue_summary.csv"
    )

    return df.to_dict(
        orient="records"
    )

@app.get("/retention")
def retention():

    df = pd.read_csv(
        "../exports/retention_metrics.csv"
    )

    return df.to_dict(
        orient="records"
    )

@app.get("/categories")
def categories():

    df = pd.read_csv(
        "../exports/category_performance.csv"
    )

    return df.to_dict(
        orient="records"
    )