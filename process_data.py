import pandas as pd
import glob
import os

data_path = os.path.join('data', '*.csv')
csv_files = glob.glob(data_path)

dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    df['product'] = df['product'].str.strip().str.lower()
    df = df[df['product'] == 'pink morsel']

    # Convert to numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['sales'] = df['quantity'] * df['price']

    df = df[['sales', 'date', 'region']]
    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv('output.csv', index=False)
print("✅ output.csv created successfully!")
