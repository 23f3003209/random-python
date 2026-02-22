from fastapi import FastAPI
import requests
import pandas as pd
from utils import get_random_quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/quote")
def quote():
    return {"quote": get_random_quote()}

@app.get("/data")
def data():
    df = pd.DataFrame({
        "name": ["A", "B", "C"],
        "score": [10, 20, 30]
    })
    return df.to_dict()
