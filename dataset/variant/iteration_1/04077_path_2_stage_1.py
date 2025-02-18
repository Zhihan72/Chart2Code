import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Pistachio']
parlors = ['Central Park', 'Downtown', 'Suburban', 'Beachfront']

# Monthly revenue data for each parlor (in thousands of dollars)
revenue_data = {
    'Central Park': [12, 15, 14, 10, 16, 11],
    'Downtown': [9, 12, 11, 8, 13, 10],
    'Suburban': [10, 11, 9, 7, 12, 8],
    'Beachfront': [14, 16, 15, 12, 18, 14]
}

# Single color for all bars
single_color = '#4682B4'  # Steel blue

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.18

# Plot bars for each parlor using the single defined color
for i, parlor in enumerate(parlors):
    positions = np.arange(len(flavors)) + i * bar_width
    ax.bar(positions, revenue_data[parlor], width=bar_width, color=single_color, label=parlor, edgecolor='black')

ax.set_xlabel('Ice Cream Flavors', fontsize=12)
ax.set_ylabel('Monthly Revenue (in thousands of $)', fontsize=12)
ax.set_title('Monthly Revenue from Ice Cream Flavors Across Different Parlors', fontsize=16, fontweight='bold', pad=15)
ax.set_xticks(np.arange(len(flavors)) + bar_width * 1.5)
ax.set_xticklabels(flavors, rotation=45, ha='right')
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

for i, parlor in enumerate(parlors):
    positions = np.arange(len(flavors)) + i * bar_width
    for j, value in enumerate(revenue_data[parlor]):
        ax.text(positions[j], value + 0.3, str(value), ha='center', va='bottom', fontsize=10, color='black')

ax.legend(title='Parlors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()