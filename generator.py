import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Configuration: How many rows are we gonna use?
TOTAL_ROWS = 5000

# 2. Messy Data
names = ["juan perez", "MARIA LOPEZ", "  carlos ruiz", "Ana Silva", "luis torres", "Pedro Marmol"]
categories = ["Layer 1", "Layer 2", "Software", "Configuration"]
statuses = ["S", "No", "Yes", "N", "1", "0", "y"]

data = []

print(f"Generating {TOTAL_ROWS} rows of messy data...")

for i in range(TOTAL_ROWS):
    # Generate a random date within the last 30 days
    days_back = random.randint(0, 30)
    date_obj = datetime.now() - timedelta(days=days_back)
    
    # Intentionally messy date formats
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%m-%d-%y"]
    formatted_date = date_obj.strftime(random.choice(date_formats))
    
    # Realistic latency with intentional errors (negative values)
    latency = random.randint(-100, 500) 
    
    # Building rows
    row = {
        "ticket_id": 1000 + i,
        "customer_name": random.choice(names),
        "opening_date": formatted_date,
        "latency_ms": latency,
        "is_resolved": random.choice(statuses),
        "issue_category": random.choice(categories)
    }
    data.append(row)

# 3. Creating DataFrame and Export
df = pd.DataFrame(data)
df.to_csv('raw_isp_data.csv', index=False)

print("---")
print(f"Success! 'raw_isp_data.csv' has been created with {TOTAL_ROWS} rows.")