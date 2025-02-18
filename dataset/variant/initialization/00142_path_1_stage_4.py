import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.arange(2010, 2021)

italian_cuisine = [65, 68, 70, 72, 75, 80, 85, 88, 92, 95, 98]
chinese_cuisine = [70, 72, 75, 78, 80, 85, 88, 90, 92, 93, 94]
indian_cuisine = [50, 55, 60, 65, 70, 74, 80, 85, 90, 92, 95]
mexican_cuisine = [60, 63, 65, 67, 70, 73, 76, 80, 84, 87, 90]
middle_eastern_cuisine = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
japanese_cuisine = [40, 42, 45, 48, 52, 56, 60, 65, 70, 75, 78]

# Positive and Negative offsets from the central axis (zero)
pos_values = np.array([italian_cuisine, chinese_cuisine, indian_cuisine])
neg_values = np.array([mexican_cuisine, middle_eastern_cuisine, japanese_cuisine])

# Labels for stacked bar sections
labels_pos = ['Italian', 'Chinese', 'Indian']
labels_neg = ['Mexican', 'Middle-Eastern', 'Japanese']

# Colors for the sections
colors_pos = ['lightgreen', 'gold', 'salmon']
colors_neg = ['peru', 'pink', 'skyblue']

ind = np.arange(len(years))

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Iterate over positive and negative values to stack the bars
for i in range(pos_values.shape[0]):
    ax.barh(ind, pos_values[i], left=np.sum(pos_values[:i], axis=0), color=colors_pos[i], label=labels_pos[i])

for i in range(neg_values.shape[0]):
    ax.barh(ind, -neg_values[i], left=-np.sum(neg_values[:i], axis=0), color=colors_neg[i], label=labels_neg[i])

# Setup the axes
ax.set_yticks(ind)
ax.set_yticklabels(years)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_xlabel('Popularity Index Divergence')
ax.set_title('Diverging Bar Chart of Culinary Types Popularity (2010-2020)')
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Add the legend
ax.legend(title='Cuisine Popularity', fontsize=10)

plt.tight_layout()
plt.show()