import matplotlib.pyplot as plt
import numpy as np

regions = ['Americas', 'Europe', 'Asia-Pacific']

# Adjust consumption data for diverging effect
consumption_data = np.array([
    [20, 15, -35],  
    [35, -30, -5],  
    [-20, 30, -10]  
])

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.5
indices = np.arange(len(regions))
bottoms = np.zeros(len(regions))
colors = ['#D2B48C', '#DEB887', '#8B4513']

# Plot diverging bars
for i in range(consumption_data.shape[1]):
    ax.bar(indices, consumption_data[:, i], bar_width, bottom=bottoms,
           color=colors[i], edgecolor='grey')
    bottoms += consumption_data[:, i]

ax.set_xticks(indices)
ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()