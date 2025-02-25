import matplotlib.pyplot as plt
import numpy as np

fruits = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries", "Figs", "Grapes"]
production_volume = [2500, 1800, 950, 1130, 750, 640, 1420]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the horizontal bar chart
ax.barh(fruits, production_volume, color='#87CEEB', edgecolor='grey', linestyle='--')

# Customize the appearance
ax.set_xlim(0, max(production_volume) + 350)
ax.set_yticks(np.arange(len(fruits)))
ax.set_yticklabels(fruits, fontsize=10, fontweight='normal')
ax.grid(axis='x', color='grey', linestyle=':', linewidth=0.8, alpha=0.9)

# Add a legend
ax.legend(['Production Volume'], loc='lower right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()