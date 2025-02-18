import matplotlib.pyplot as plt
import numpy as np

regions = ['Americas', 'Europe', 'Asia-Pacific']
coffee_types = ['Espresso', 'Latte', 'Cold Brew']

# Adjust consumption data to be positive and negative values around 0 for diverging effect
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

# Plot diverging bars for each coffee type
for i, coffee_type in enumerate(coffee_types):
    ax.bar(indices, consumption_data[:, i], bar_width, bottom=bottoms, label=coffee_type, 
           color=colors[i], edgecolor='grey')
    bottoms += consumption_data[:, i]  # Update bottoms to stack bars

ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Percentage', fontsize=12)
ax.set_title('Regional Coffee Consumption\nDiverging Breakdown: 2023', fontsize=16, weight='bold')
ax.set_xticks(indices)
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)
ax.axhline(0, color='black', linewidth=0.8)
ax.legend(title='Coffee Types', fontsize=10)

plt.tight_layout()
plt.show()