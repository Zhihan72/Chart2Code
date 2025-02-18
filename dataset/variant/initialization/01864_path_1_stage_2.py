import matplotlib.pyplot as plt
import numpy as np

decades = ['1990s', '2000s', '2010s', '2020s']

solar_energy = [5, 15, 50, 120]
wind_energy = [10, 25, 60, 150]
hydroelectric = [100, 120, 150, 160]
biomass_energy = [20, 30, 40, 55]

energy_data = np.array([solar_energy, wind_energy, hydroelectric, biomass_energy])

fig, ax = plt.subplots(figsize=(12, 7))

# Altered colors and order
colors = ['#20B2AA', '#87CEEB', '#FFD700', '#FFA07A']

# Diverse styles for variety
ax.stackplot(decades, energy_data, labels=['Wind', 'Biomass', 'Solar', 'Hydroelectric'], colors=colors, alpha=0.7)

# Title and label adjustments
ax.set_title('Renewable Energy Over the Decades', fontsize=18, fontweight='normal', pad=10)
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Contribution (Units)', fontsize=14)

# Legend customization
ax.legend(loc='lower right', fontsize=11, title='Type of Energy', bbox_to_anchor=(0.5, -0.2))

# Modified grid and border
ax.grid(True, linestyle='-', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.show()