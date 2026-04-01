from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(title="Enterprise Scraper API", version="1.0.0")

DATA_PATH = "data/quotes_enterprise.csv"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Enterprise Web Scraping Data API"}

@app.get("/data")
def get_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH, sep=";")
        return df.to_dict(orient="records")
    return {"error": "No data available yet. Run the scraper first."}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "scraper-api"}
