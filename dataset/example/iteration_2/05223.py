import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The local community garden has been tracking the yield of various vegetables over the past decade.
# The data aims to explore the trends in vegetable yields to help improve community gardening practices.

# Define years from 2011 to 2020
years = np.arange(2011, 2021)

# Yields of different vegetables in kilograms
tomatoes = np.array([50, 55, 60, 58, 62, 64, 65, 70, 75, 80])
carrots = np.array([40, 42, 45, 47, 49, 52, 50, 55, 58, 60])
cucumbers = np.array([30, 32, 35, 37, 38, 40, 42, 45, 48, 50])
lettuce = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

# Setup the main plot
fig, ax = plt.subplots(figsize=(14, 8))

# Bar chart for vegetable yields
width = 0.2  # Width of each bar
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

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()