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

colors = ['#4682B4', '#B42222', '#2E8B57', '#D2691E', '#FF7F50']

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.35

# Starting point for the stacks
bottom_data = np.zeros(len(flavors))

# Plotting the stacked bars
for i, parlor in enumerate(parlors):
    ax.bar(flavors, revenue_data[parlor], width=bar_width, color=colors[i], edgecolor='black', label=parlor, bottom=bottom_data)
    # Update the bottom position for the next parlor's data
    bottom_data += revenue_data[parlor]

ax.set_xlabel('Flavors', fontsize=12)
ax.set_ylabel('Revenue ($k)', fontsize=12)
ax.set_title('Monthly Revenue by Flavor & Parlor', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(np.arange(len(flavors)))
ax.set_xticklabels(flavors, rotation=45, ha='right')
ax.legend(title='Parlors')  # Add legend to differentiate each parlor's bar

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')

plt.tight_layout()
plt.show()