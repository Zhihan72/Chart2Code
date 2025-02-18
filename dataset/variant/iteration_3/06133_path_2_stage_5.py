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

# New set of colors
colors = ['#2196F3', '#F44336', '#FFC107', '#8BC34A', '#FF9800']  # New colors
bar_height = 0.15

for idx in range(len(stores)):
    ax1.barh(years + np.array([idx])*bar_height, revenue[:, idx], height=bar_height, 
             color=colors[idx % len(colors)], alpha=0.7)

# Remove textual elements
ax1.set_xticks([])
ax1.set_yticks([])
ax1.legend().set_visible(False)
ax1.grid(False)

plt.tight_layout()
plt.show()