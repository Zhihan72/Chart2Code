import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = np.array([50, 60, 75, 95, 110, 130, 150, 180, 210, 240, 280])

plt.figure(figsize=(12, 6))

# Randomly altered stylistic elements in the plot
plt.plot(years, solar_capacity, marker='s', linestyle='--', color='green', label='Solar Energy', linewidth=3)

for i, (x, y) in enumerate(zip(years, solar_capacity)):
    plt.annotate(f'{y} MW', (x, y), textcoords="offset points", xytext=(-15, 5), ha='center', fontsize=8, color='green')

plt.title('Solar Energy Adoption in EcoVille\n(2010-2020)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Installed Capacity (MW)', fontsize=12)

plt.legend(loc='lower right', frameon=True)
plt.grid(True, linestyle='-', alpha=0.3)

plt.axvline(x=2015, color='purple', linestyle='-', linewidth=1.5)
plt.text(2015, max(solar_capacity) + 30, 'Paris Agreement', ha='center', color='purple')

plt.tight_layout()
plt.show()