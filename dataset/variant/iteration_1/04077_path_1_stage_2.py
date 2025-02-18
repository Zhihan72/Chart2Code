import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Pistachio']

parlor_data = {
    'Central Park': [12, 15, 14, 10, 16, 11],
    'Downtown': [-9, -12, -11, -8, -13, -10],
    'Suburban': [10, 11, 9, 7, 12, 8],
    'Beachfront': [-14, -16, -15, -12, -18, -14]
}

# Shuffled colors
flavor_colors = ['#43A047', '#E91E63', '#A5D6A7', '#D4A017', '#3E2723', '#795548']

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.6

for i, (parlor, revenue) in enumerate(parlor_data.items()):
    offset = i * bar_width
    ax.barh(np.arange(len(flavors)) + offset, revenue, color=flavor_colors, 
            edgecolor='black', height=bar_width, label=parlor)

ax.set_yticks(np.arange(len(flavors)) + (len(parlor_data) * bar_width) / 2 - bar_width / 2)
ax.set_yticklabels(flavors)
ax.set_xlabel('Monthly Revenue (in thousands of $)', fontsize=12)
ax.set_title('Diverging Monthly Revenue from Ice Cream Flavors', fontsize=16, fontweight='bold')

ax.legend(title='Parlors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()