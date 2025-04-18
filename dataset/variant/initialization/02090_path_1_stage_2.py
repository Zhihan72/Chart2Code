import matplotlib.pyplot as plt
import numpy as np

# Data for Renewable Energy Adoption in EcoVille
years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])

# Create the plot
plt.figure(figsize=(12, 6))

# Plotting the Solar Energy data
plt.plot(years, solar_capacity, marker='o', linestyle='-', color='blue', label='Solar Energy', linewidth=2)

# Annotate each data point for Solar Energy
for i, (x, y) in enumerate(zip(years, solar_capacity)):
    plt.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10, 10), ha='center', fontsize=9, color='blue')

# Title and labels
plt.title('Solar Energy Adoption in EcoVille\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Installed Capacity (MW)', fontsize=12)

# Legend and grid
plt.legend(loc='upper left', frameon=False)
plt.grid(True, linestyle='--', alpha=0.5)

# Adding a milestone marker
plt.axvline(x=2015, color='gray', linestyle=':', linewidth=1)
plt.text(2015, max(solar_capacity) + 20, 'Paris Agreement', ha='center', color='gray')

# Ensure layout is tidy and avoid overlap
plt.tight_layout()

# Show the plot
plt.show()