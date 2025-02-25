import matplotlib.pyplot as plt
import numpy as np

# Fruits and their production volumes in tons - Extended with additional fruits
fruits = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries", "Figs", "Grapes"]
production_volume = [2500, 1800, 950, 1130, 750, 640, 1420]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the vertical bar chart with altered stylistic elements
ax.bar(fruits, production_volume, color='#87CEEB', edgecolor='grey', width=0.5, linestyle='--')

# Customize the appearance
ax.set_ylim(0, max(production_volume) + 350)
ax.set_xticks(np.arange(len(fruits)))
ax.set_xticklabels(fruits, fontsize=10, fontweight='normal')
ax.grid(axis='y', color='grey', linestyle=':', linewidth=0.8, alpha=0.9)

# Add a legend
ax.legend(['Production Volume'], loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()