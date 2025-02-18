import matplotlib.pyplot as plt
import numpy as np

# Data
fruit_types = ['Apples', 'Bananas', 'Cherries', 'Grapes', 'Oranges', 'Pineapples']
preferences_percentages = [25, 20, 15, 30, 10, 18]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb347']

# Create figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Side Bar Chart: Detailed View of Grapes Varieties
grape_subtypes = ['Crimson Grapes', 'Emerald Grapes', 'Onyx Grapes', 'Misty Grapes']
grape_preferences = [60, 20, 10, 10]
grape_colors = ['#ff6666', '#99ff99', '#6666ff', '#ffb3e6']
y_pos = np.arange(len(grape_subtypes))

ax[0].barh(y_pos, grape_preferences, color=grape_colors, edgecolor='black')
ax[0].set_yticks(y_pos)
ax[0].set_yticklabels(grape_subtypes)
ax[0].invert_yaxis()
ax[0].set_xlabel('Proportion', fontsize=12)
for index, value in enumerate(grape_preferences):
    ax[0].text(value + 2, index, f'{value}%', va='center', ha='left', fontsize=10)
ax[0].set_title('Varieties of Grapes Consumption Comparison', fontsize=14, fontweight='bold', pad=20)

# Main Bar Chart: Sorted Fruit Choices
sorted_indices = np.argsort(preferences_percentages)
sorted_fruits = [fruit_types[i] for i in sorted_indices]
sorted_preferences = [preferences_percentages[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]
x_pos = np.arange(len(sorted_fruits))

ax[1].bar(x_pos, sorted_preferences, color=sorted_colors, edgecolor='black')
ax[1].set_xticks(x_pos)
ax[1].set_xticklabels(sorted_fruits)
ax[1].set_ylabel('Proportion', fontsize=12)
for index, value in enumerate(sorted_preferences):
    ax[1].text(index, value + 1, f'{value}%', va='bottom', ha='center', fontsize=10)
ax[1].set_title('Sorted Popular Fruit Choices at Local Bazaar', fontsize=14, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()