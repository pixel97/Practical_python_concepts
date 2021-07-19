
import pandas as pd
import os

cwd = os.getcwd()
DATA_DIR = os.path.join(cwd,'data')
print(DATA_DIR)

os.listdir(DATA_DIR)

my_items = [{"category": "Thriller", "title": "My favorites"}, {"category":"RomCom","title": "Love"}]
df = pd.DataFrame(my_items)
df.head()

my_data = os.path.join(DATA_DIR, '2020.csv')
print(os.path.exists(my_data))

df_2020 = pd.read_csv(my_data)
df_2020.head()
print("Data Loaded")



