import matplotlib.pyplot as plt
import numpy as np

# Data for Renewable Energy Adoption in EcoVille
years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])

# Set up single plot as Wind Energy is removed
fig, ax1 = plt.subplots(figsize=(8, 6))

# Subplot for Solar Energy
ax1.plot(years, solar_capacity, marker='o', linestyle='-', color='orange', label='Solar Energy', linewidth=2)

for i, (x, y) in enumerate(zip(years, solar_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='orange')

ax1.set_title('Solar Energy Adoption in EcoVille\n(2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Installed Capacity (MW)', fontsize=10)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.axvline(x=2015, color='gray', linestyle=':', linewidth=1)
ax1.text(2015, max(solar_capacity) + 20, 'Paris Agreement', ha='center', color='gray')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()