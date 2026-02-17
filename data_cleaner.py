import pandas as pd
import numpy as np

# 1. Loading raw data
print("Starting data cleaning process...")
df = pd.read_csv('raw_isp_data.csv')

# 2. Cleaning Customer Names
df['customer_name'] = df['customer_name'].str.strip().str.title()

# 3. Standardize Dates
df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce')

# 4. Fixing Technical Anomalies such as negative latency
mean_latency = int(df[df['latency_ms'] > 0]['latency_ms'].mean())
df.loc[df['latency_ms'] < 0, 'latency_ms'] = mean_latency

# 5. Map Resolution Status to Booleans (1/0)
status_map = {'S': 1, 'Yes': 1, '1': 1, 'y': 1, 'No': 0, 'N': 0, '0': 0}
df['is_resolved'] = df['is_resolved'].map(status_map).fillna(0).astype(int)

# 6. Export Clean Data
df.to_csv('cleaned_isp_report.csv', index=False)
print(f"Success! Processed {len(df)} rows into 'cleaned_isp_report.csv'.")