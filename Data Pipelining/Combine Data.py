

import pandas as pd
import os


cwd = os.getcwd()
DATA_DIR = os.path.join(cwd,'data')
CACHE_DIR = os.path.join(DATA_DIR,'cache')
os.makedirs(CACHE_DIR, exist_ok=True)
print(DATA_DIR)
print(CACHE_DIR)

for filename in os.listdir(DATA_DIR):
    print(filename)

df = pd.read_csv(os.path.join(DATA_DIR,'2020.csv'))
df.head()

df['Year'] = 2020
df.head()

entire_df = []
csv_files = [x for x in os.listdir(DATA_DIR) if x.endswith(".csv")]
for filename in csv_files:
    year = filename.replace(".csv", " ")
    csv_path = os.path.join(DATA_DIR,filename)
    df_files = pd.read_csv(csv_path)
    df_files['filename'] = filename
    df_files['year'] = year
    entire_df.append(df_files)
    print(df_files.head())

dataset = pd.concat(entire_df)
dataset.tail()

data = os.path.join(CACHE_DIR,'movies_dataset.csv')
dataset.to_csv(data,index=False)
print("Data Combined")



