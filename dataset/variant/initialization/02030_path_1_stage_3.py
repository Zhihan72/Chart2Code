import matplotlib.pyplot as plt
import numpy as np

# Data for the eco-friendly beverage production
beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]
colors = ['#8FD14F', '#FFD700', '#FF69B4', '#40E0D0', '#BA55D3']

# Sorting the data in descending order based on production volumes
sorted_indices = np.argsort(production_volumes)[::-1]
beverages = [beverages[i] for i in sorted_indices]
production_volumes = [production_volumes[i] for i in sorted_indices]
colors = [colors[i] for i in sorted_indices]

# Plotting the sorted bar chart without texts
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(beverages, production_volumes, color=colors, alpha=0.85, edgecolor='black')

# Disable axis labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()