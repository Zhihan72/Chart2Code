import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Pistachio']

parlor_data = {
    'Central Park': [15, 12, 16, 14, 11, 10],
    'Downtown': [-12, -9, -13, -11, -10, -8],
    'Suburban': [11, 10, 12, 9, 8, 7],
    'Beachfront': [-16, -14, -18, -15, -14, -12]
}

flavor_colors = ['#43A047', '#E91E63', '#A5D6A7', '#D4A017', '#3E2723', '#795548']

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.6

for i, (parlor, revenue) in enumerate(parlor_data.items()):
    offset = i * bar_width
    ax.barh(np.arange(len(flavors)) + offset, revenue, color=flavor_colors, 
            edgecolor='black', height=bar_width)

plt.tight_layout()
plt.show()