import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
stores = ["Store A", "Store B", "Store C", "Store D", "Store E"]

revenue = np.array([
    [12, 11, 13, 16, 15], 
    [9, 11, 8, 13, 12],    
    [16, 14, 17, 19, 21],  
    [14, 13, 15, 16, 17],  
    [10, 12, 9, 13, 14],   
])

fig, ax1 = plt.subplots(figsize=(14, 8))
colors = ['#33FF57', '#FF5733', '#A133FF', '#3357FF', '#FF33A1']
bar_height = 0.15

for idx, store in enumerate(stores):
    ax1.barh(years + np.array([idx])*bar_height, revenue[:, idx], height=bar_height, 
             color=colors[idx % len(colors)], alpha=0.7, label=f"{store} Revenue")

ax1.set_title('Retail Chain Performance Analysis:\nRevenue per Year (2018-2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Revenue (in millions)', fontsize=12)
ax1.set_ylabel('Stores', fontsize=12)
ax1.set_yticks(years + bar_height * (len(stores) - 1) / 2)
ax1.set_yticklabels(years)

ax1.legend(title='Stores', loc='upper left', fontsize=10, frameon=False)

ax1.grid(False)

plt.tight_layout()
plt.show()