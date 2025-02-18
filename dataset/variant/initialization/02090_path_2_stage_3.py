import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])

plt.figure(figsize=(12, 6))

# Shuffled color is not used anymore.
plt.plot(years, solar_capacity, marker='o', linestyle='-', color='green', linewidth=2)

for i, (x, y) in enumerate(zip(years, solar_capacity)):
    plt.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9, color='green')

plt.title('Renewable Energy Adoption in EcoVille\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Installed Capacity (MW)', fontsize=12)

# Removed legend, grid, borders
plt.axvline(x=2015, color='gray', linestyle=':', linewidth=1)
plt.text(2015, max(solar_capacity) + 20, 'Paris Agreement', ha='center', color='gray')

plt.tight_layout()

plt.show()