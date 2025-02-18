import matplotlib.pyplot as plt
import numpy as np

# Data
fruit_types = ['Apples', 'Bananas', 'Cherries', 'Grapes', 'Oranges']
preferences_percentages = [25, 20, 15, 30, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Side Bar Chart: Detailed View of Grapes Varieties
grape_subtypes = ['Crimson Grapes', 'Emerald Grapes', 'Onyx Grapes']
grape_preferences = [60, 25, 15]
grape_colors = ['#ff6666', '#99ff99', '#6666ff']
y_pos = np.arange(len(grape_subtypes))

ax[0].barh(y_pos, grape_preferences, color=grape_colors, edgecolor='black')
ax[0].set_yticks(y_pos)
ax[0].set_yticklabels(grape_subtypes)
ax[0].invert_yaxis()
ax[0].set_xlabel('Proportion', fontsize=12)
for index, value in enumerate(grape_preferences):
    ax[0].text(value + 2, index, f'{value}%', va='center', ha='left', fontsize=10)
ax[0].set_title('Varieties of Grapes Consumption Comparison', fontsize=14, fontweight='bold', pad=20)

# Main Pie Chart: General Fruit Choices
wedges1, texts1, autotexts1 = ax[1].pie(
    preferences_percentages, labels=fruit_types, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, explode=(0.1, 0, 0, 0.1, 0), shadow=True
)
centre_circle1 = plt.Circle((0, 0), 0.70, fc='white')
ax[1].add_artist(centre_circle1)
ax[1].axis('equal')
ax[1].set_title('Popular Fruit Choices at Local Bazaar', fontsize=14, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()