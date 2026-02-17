import pandas as pd
import random
from datetime import datetime, timedelta

TOTAL_ROWS = 5000
categories = ["Layer 1", "Layer 2", "Software", "Configuration"]
names = ["juan perez", "MARIA LOPEZ", "  carlos ruiz", "Ana Silva", "luis torres", "Pedro Marmol"]
statuses = ["S", "No", "Yes", "N", "1", "0", "y"]

data = []

for i in range(TOTAL_ROWS):
    category = random.choice(categories)
    
    # Logic: Varied latency per category
    if category == "Layer 1":
        latency = random.randint(200, 800)
    elif category == "Layer 2":
        latency = random.randint(100, 400)
    elif category == "Configuration":
        latency = random.randint(50, 200)
    else:
        latency = random.randint(20, 100)
    
    # Inject 10% errors
    if random.random() < 0.1:
        latency = random.randint(-100, -1)

    date_obj = datetime.now() - timedelta(days=random.randint(0, 30))
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%m-%d-%y"]
    
    row = {
        "ticket_id": 1000 + i,
        "customer_name": random.choice(names),
        "opening_date": date_obj.strftime(random.choice(date_formats)),
        "latency_ms": latency,
        "is_resolved": random.choice(statuses),
        "issue_category": category
    }
    data.append(row)

pd.DataFrame(data).to_csv('raw_isp_data.csv', index=False)
print("Step 1: 'raw_isp_data.csv' created.")