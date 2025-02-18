import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie', 'Pistachio']
parlors = ['Central', 'Downtown', 'Suburban', 'Beach', 'Campus']

revenue_data = {
    'Central': [12, 15, 14, 10, 16, 11],
    'Downtown': [9, 12, 11, 8, 13, 10],
    'Suburban': [10, 11, 9, 7, 12, 8],
    'Beach': [14, 16, 15, 12, 18, 14],
    'Campus': [11, 13, 12, 9, 14, 11]
}

single_color = '#4682B4'

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15

for i, parlor in enumerate(parlors):
    positions = np.arange(len(flavors)) + i * bar_width
    ax.bar(positions, revenue_data[parlor], width=bar_width, color=single_color, edgecolor='black')

ax.set_xlabel('Flavors', fontsize=12)
ax.set_ylabel('Revenue ($k)', fontsize=12)
ax.set_title('Monthly Revenue by Flavor & Parlor', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(np.arange(len(flavors)) + bar_width * 2)
ax.set_xticklabels(flavors, rotation=45, ha='right')

for i, parlor in enumerate(parlors):
    positions = np.arange(len(flavors)) + i * bar_width
    for j, value in enumerate(revenue_data[parlor]):
        ax.text(positions[j], value + 0.3, str(value), ha='center', va='bottom', fontsize=10, color='black')

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')

plt.tight_layout()
plt.show()