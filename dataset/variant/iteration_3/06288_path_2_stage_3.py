import matplotlib.pyplot as plt
import numpy as np

# Data
species = ["Andronian", "Xylok", "Zepherite", "Fermian", "Galzor", 
           "Ignitoid", "Hydrixian", "Eldarian", "Nebulon", "Vortix"]
heights = np.array([2.3, 1.8, 2.6, 1.5, 2.1, 3.0, 2.8, 2.2, 1.9, 2.4])
weights = np.array([120, 95, 150, 75, 110, 180, 170, 140, 100, 130])

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Horizontal bar chart
ax.barh(species, weights, color='blue', edgecolor='w', linewidth=0.5)

# Setting up title and labels
ax.set_title("The Galactic Fauna: Study of Fictional Alien Species", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Weight (kg)", fontsize=12)
ax.set_ylabel("Species", fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()