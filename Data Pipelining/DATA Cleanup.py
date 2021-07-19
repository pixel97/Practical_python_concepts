
import pandas as pd
import os

cwd = os.getcwd()
DATA_DIR = os.path.join(cwd,'data')
CACHE_DIR = os.path.join(DATA_DIR,'cache')
os.makedirs(CACHE_DIR, exist_ok=True)
working_file = os.path.join(CACHE_DIR,'movies_dataset.csv')
output_file = os.path.join(CACHE_DIR,'movies_dataset_cleane.csv')
print(DATA_DIR)
print(CACHE_DIR)

df = pd.read_csv(working_file)
df.head()

df['Domestic %'] = df['%']
df['Foreign %'] = df['%.1']
df.drop(columns=['%','%.1'],inplace=True)

df['Rank'] = -1
df.head()

clean_cols = ['Worldwide','Domestic','Foreign']
def clean_col(row):
    for col in clean_cols:
        row[col] = row[col].replace("$","").replace(",", "")
        try:
            row[col] = int(row[col])
        except:
            row[col] = 0
    return row

df_cleaned = df.apply(clean_col,axis=1)
df_cleaned.head()

df_cleaned.dtypes


df_cleaned.sort_values(by=['Worldwide'],inplace=True,ascending=False)
df_cleaned.reset_index(inplace=True,drop=True)
df_cleaned.head()


df_cleaned['Rank'] = df_cleaned.index + 1
df_cleaned.head()

df_cleaned.to_csv(output_file,index=False)
print("Data Cleaned")