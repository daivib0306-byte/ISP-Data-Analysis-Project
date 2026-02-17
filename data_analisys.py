import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_isp_report.csv')

# Insights
avg_latency = df.groupby('issue_category')['latency_ms'].mean().sort_values(ascending=False)
res_rate = df['is_resolved'].mean() * 100

# Visual
plt.figure(figsize=(10, 6))
avg_latency.plot(kind='bar', color='skyblue', edgecolor='navy')
plt.title('Average Network Latency by Category')
plt.ylabel('Latency (ms)')
plt.tight_layout()
plt.savefig('latency_analysis.png')

print("Step 3: Analysis complete. Results printed and 'latency_analysis.png' saved.")
print(f"\nAverage Latency:\n{avg_latency}")
print(f"\nGlobal Resolution Rate: {res_rate:.2f}%")