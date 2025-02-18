import matplotlib.pyplot as plt
import numpy as np

# Define ingredient names
ingredients = ['Dragon Scales', 'Unicorn Horn', 'Phoenix Feathers', 'Mandrake Root', 'Elven Elixir']

# Constructing dataset for each ingredient's potency over various batches
potencies = [
    [50, 55, 53, 52, 51, 56, 54, 58, 52, 59],
    [75, 78, 77, 80, 79, 76, 81, 82, 83, 78],
    [65, 68, 70, 67, 66, 69, 71, 72, 65, 68],
    [40, 42, 41, 43, 39, 44, 40, 45, 42, 41],
    [90, 95, 92, 93, 91, 96, 94, 97, 93, 95]
]

# New dataset for the overlay line plot representing average potency under different conditions
average_potencies = [54, 79, 67, 43, 92]

# Create a vertical box plot
fig, ax = plt.subplots(figsize=(12, 8))

# Boxplot data
boxes = ax.boxplot(potencies, patch_artist=True, notch=True, vert=True, showmeans=True)

# Overlay line plot
ax.plot(range(1, len(average_potencies) + 1), average_potencies, marker='s', linestyle='-', color='darkred', linewidth=2)

# Set x-tick labels
ax.set_xticks(range(1, len(ingredients) + 1))
ax.set_xticklabels(ingredients, fontsize=10, rotation=15, ha='right')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()