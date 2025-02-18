import matplotlib.pyplot as plt
import numpy as np

fruit_types = ['Appl', 'Bana', 'Cher', 'Grap', 'Oran']
preferences_percentages = [30, 15, 25, 10, 20]
y_pos_fruits = np.arange(len(fruit_types))

grape_subtypes = ['Red', 'Green', 'Black']
grape_preferences = [25, 15, 60]
y_pos_grapes = np.arange(len(grape_subtypes))

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Set a single color for all bars
single_color = '#66b3ff'

# Horizontal bar chart for grape preferences
ax[0].barh(y_pos_grapes, grape_preferences, color=single_color, edgecolor='black')
ax[0].set_yticks(y_pos_grapes)
ax[0].set_yticklabels(grape_subtypes)
ax[0].invert_yaxis()
ax[0].set_xlabel('%', fontsize=12)

for index, value in enumerate(grape_preferences):
    ax[0].text(value + 2, index, f'{value}%', va='center', ha='left', fontsize=10)

ax[0].set_title('Grape Dist.', fontsize=14, fontweight='bold', pad=20)

# Horizontal bar chart for community fruit preferences
ax[1].barh(y_pos_fruits, preferences_percentages, color=single_color, edgecolor='black')
ax[1].set_yticks(y_pos_fruits)
ax[1].set_yticklabels(fruit_types)
ax[1].invert_yaxis()
ax[1].set_xlabel('%', fontsize=12)

for index, value in enumerate(preferences_percentages):
    ax[1].text(value + 1, index, f'{value}%', va='center', ha='left', fontsize=10)

ax[1].set_title('Fruit Pref. Market', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()