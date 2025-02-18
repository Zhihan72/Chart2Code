import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q1', 'Q2', 'Q3', 'Q4',
    'Q1', 'Q2', 'Q3'
])

projected_revenues = np.array([150, 160, 170, 180, 192, 205, 215])

# Sort the data in ascending order
sorted_indices = np.argsort(projected_revenues)
quarters_sorted = quarters[sorted_indices]
projected_revenues_sorted = projected_revenues[sorted_indices]

plt.figure(figsize=(12, 6))

# Manually changed the color set to different colors
colors = ['#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', '#FF4500', '#2E8B57']

# Plot a bar chart with sorted data
plt.bar(quarters_sorted, projected_revenues_sorted, color=colors, label='Proj. Revenue')

plt.title('Sorted Revenue Forecast', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Revenue (Million $)', fontsize=12)

plt.xticks(rotation=45)
plt.grid(True, linestyle='-.', alpha=0.8)
plt.legend(loc='upper left', fontsize=8)

plt.tight_layout()
plt.show()