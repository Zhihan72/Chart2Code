import matplotlib.pyplot as plt
import numpy as np

# Define years from 2011 to 2020
years = np.arange(2011, 2021)

# Manually shuffled yields of different vegetables in kilograms
tomatoes = np.array([62, 60, 70, 55, 50, 75, 65, 64, 58, 80])
carrots = np.array([52, 49, 42, 60, 40, 50, 58, 55, 47, 45])
cucumbers = np.array([35, 48, 30, 42, 32, 37, 50, 45, 40, 38])
lettuce = np.array([32, 38, 22, 34, 20, 24, 26, 28, 36, 30])

# Setup the main plot
fig, ax = plt.subplots(figsize=(14, 8))

# Bar chart for vegetable yields
width = 0.2
ax.bar(years - width * 1.5, tomatoes, width, label='Tomatoes', color='tomato')
ax.bar(years - width / 2, carrots, width, label='Carrots', color='orange')
ax.bar(years + width / 2, cucumbers, width, label='Cucumbers', color='green')
ax.bar(years + width * 1.5, lettuce, width, label='Lettuce', color='lightgreen')

# Titles and labels
ax.set_title('Community Garden Vegetable Yields (2011-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Yield (kg)', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 100, 10))
ax.grid(True, linestyle='--', alpha=0.5)

# Adding legend
ax.legend(loc='upper left', fontsize=10, edgecolor='black', title='Vegetables')

plt.tight_layout()
plt.show()