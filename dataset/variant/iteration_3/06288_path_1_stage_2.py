import matplotlib.pyplot as plt
import numpy as np

# Data
species = ["Andronian", "Xylok", "Zepherite", "Fermian", "Galzor", 
           "Ignitoid", "Hydrixian", "Eldarian", "Nebulon", "Vortix",
           "Lithorian", "Plazmoid", "Quarkian", "Solaran", "Astralan"]

# Weights (in kilograms)
weights = np.array([120, 95, 150, 75, 110, 180, 170, 140, 100, 130,
                    115, 185, 85, 190, 135])

# Colors based on gravity
gravities = np.array([0.85, 0.95, 1.1, 1.25, 1.0, 0.9, 1.3, 1.15, 0.98, 1.05,
                      1.1, 1.08, 0.87, 1.2, 0.99])

fig, ax = plt.subplots(figsize=(12, 8))

# Horizontal bar chart
bar = ax.barh(species, weights, color=plt.cm.viridis(gravities / max(gravities)), edgecolor='w')

# Setting up title and labels
ax.set_title("The Galactic Fauna: Weights of Fictional Alien Species", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Weight (kg)", fontsize=12)
ax.set_ylabel("Species", fontsize=12)

# Grid for readability
ax.grid(True, axis='x', linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()