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

pos_values = np.array([italian_cuisine, chinese_cuisine, indian_cuisine])
neg_values = np.array([mexican_cuisine, middle_eastern_cuisine, japanese_cuisine])

labels_pos = ['Italian', 'Chinese', 'Indian']
labels_neg = ['Mexican', 'Middle-Eastern', 'Japanese']

colors_pos = ['salmon', 'lightgreen', 'gold']  # Shuffled colors for positive
colors_neg = ['skyblue', 'peru', 'pink']       # Shuffled colors for negative

ind = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

# Change order of legend, marker types, and grid style
hatch_styles = ['', '///', '...']
for i in range(pos_values.shape[0]):
    ax.barh(ind, pos_values[i], left=np.sum(pos_values[:i], axis=0), color=colors_pos[i], 
            label=labels_pos[i], hatch=hatch_styles[i])

for i in range(neg_values.shape[0]):
    ax.barh(ind, -neg_values[i], left=-np.sum(neg_values[:i], axis=0), color=colors_neg[i], 
            label=labels_neg[i], hatch=hatch_styles[i])

ax.set_yticks(ind)
ax.set_yticklabels(years)
ax.axvline(0, color='gray', linewidth=1.5, linestyle='-')  # Changed line width and style
ax.set_xlabel('Popularity Index Divergence')
ax.set_title('Diverging Bar Chart of Culinary Types Popularity (2010-2020)')
ax.grid(axis='x', linestyle=':', linewidth=1.0, alpha=0.5)  # Changed grid style

ax.legend(title='Cuisine Popularity', fontsize=10, loc='upper left')  # Changed legend location

plt.tight_layout()
plt.show()