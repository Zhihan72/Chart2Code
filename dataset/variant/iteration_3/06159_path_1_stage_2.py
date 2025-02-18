import matplotlib.pyplot as plt
import numpy as np

# Data: Productivity (in tons) of Farm A over the years 2010 to 2020
years = np.arange(2010, 2021)
farm_a_productivity = np.array([35, 40, 42, 45, 50, 52, 55, 58, 60, 65, 70])

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot Farm A productivity
ax.plot(years, farm_a_productivity, color='green', linestyle='-', linewidth=2, marker='o')

# Add grid for better readability
ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust plot params
plt.tight_layout()

# Show the plot
plt.show()