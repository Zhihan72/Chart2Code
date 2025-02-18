import matplotlib.pyplot as plt
import numpy as np

# Data for Renewable Energy Adoption in EcoVille
years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])
wind_capacity = np.array([30, 40, 50, 70, 90, 110, 130, 150, 170, 200, 235])

fig, (ax2, ax1) = plt.subplots(2, 1, figsize=(8, 12))

# Subplot for Wind Energy
ax2.plot(years, wind_capacity, marker='s', linestyle='-', color='darkorange', label='Breeze Energy', linewidth=2)
for x, y in zip(years, wind_capacity):
    ax2.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='darkorange')
ax2.set_title('Adoption of Wind Power in EcoVille\nFrom 2010 to 2020', fontsize=14, fontweight='bold')
ax2.set_xlabel('Timeline', fontsize=10)
ax2.set_ylabel('Capacity Installed (MW)', fontsize=10)
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.5)

# Subplot for Solar Energy
ax1.plot(years, solar_capacity, marker='o', linestyle='-', color='darkcyan', label='Sun Power', linewidth=2)
for i, (x, y) in enumerate(zip(years, solar_capacity)):
    ax1.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='darkcyan')
ax1.set_title('Solar Power Adoption in EcoVille\n2010 through 2020', fontsize=14, fontweight='bold')
ax1.set_xlabel('Timeline', fontsize=10)
ax1.set_ylabel('Capacity Installed (MW)', fontsize=10)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.axvline(x=2015, color='gray', linestyle=':', linewidth=1)
ax1.text(2015, max(solar_capacity) + 20, 'Agreement in Paris', ha='center', color='gray')

plt.tight_layout()
plt.show()