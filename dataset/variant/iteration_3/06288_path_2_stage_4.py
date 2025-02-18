import matplotlib.pyplot as plt
import numpy as np

# Data
species = ["Andronian", "Xylok", "Zepherite", "Fermian", "Galzor", 
           "Ignitoid", "Hydrixian", "Eldarian", "Nebulon", "Vortix"]
weights = np.array([120, 95, 150, 75, 110, 180, 170, 140, 100, 130])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Horizontal bar chart
ax.barh(species, weights, color='blue', edgecolor='w', linewidth=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()