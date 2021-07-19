from fastapi import FastAPI
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
CACHE_DIR = os.path.join(BASE_DIR,'data\cache')
print(CACHE_DIR)

dataset = os.path.join(CACHE_DIR,'movies_dataset_cleane.csv')

app = FastAPI()

@app.get('/')
def home():
    return {"Data":"Pipeline Setup"}

@app.get('/box-office')
def read_box_office_numbers():
    df = pd.read_csv(dataset)
    return df.to_dict("Rank")


