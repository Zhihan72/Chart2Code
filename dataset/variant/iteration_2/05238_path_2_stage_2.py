import matplotlib.pyplot as plt
import numpy as np

# Fruits and their production volumes in tons
fruits = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
production_volume = [2500, 1800, 950, 1130, 750]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the vertical bar chart
ax.bar(fruits, production_volume, color='#FFA07A', edgecolor='black', width=0.6)

# Customize the appearance without text
ax.set_ylim(0, max(production_volume) + 300)
ax.set_xticks(np.arange(len(fruits)))
ax.set_xticklabels(fruits, fontsize=11, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()