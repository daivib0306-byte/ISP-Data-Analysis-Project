import pandas as pd
import numpy as np

# Load
df = pd.read_csv('raw_isp_data.csv')

# Clean names
df['customer_name'] = df['customer_name'].str.strip().str.title()

# Standardize Dates
df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce')

# Fix Latency (Convert mean to INT to avoid TypeError)
mean_latency = int(df[df['latency_ms'] > 0]['latency_ms'].mean())
df.loc[df['latency_ms'] < 0, 'latency_ms'] = mean_latency

# Map status
status_map = {'S': 1, 'Yes': 1, '1': 1, 'y': 1, 'No': 0, 'N': 0, '0': 0}
df['is_resolved'] = df['is_resolved'].map(status_map).fillna(0).astype(int)

# Export
df.to_csv('cleaned_isp_report.csv', index=False)
print("Step 2: 'cleaned_isp_report.csv' created.")