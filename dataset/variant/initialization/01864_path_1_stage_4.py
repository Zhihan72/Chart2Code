import matplotlib.pyplot as plt
import numpy as np

decades = ['1990s', '2000s', '2010s', '2020s']

solar_energy = [5, 15, 50, 120]
wind_energy = [10, 25, 60, 150]
hydroelectric = [100, 120, 150, 160]

energy_data = np.array([solar_energy, wind_energy, hydroelectric])

fig, ax = plt.subplots(figsize=(12, 7))

colors = ['#20B2AA', '#87CEEB', '#FFD700']

ax.stackplot(decades, energy_data, labels=['Wind', 'Solar', 'Hydro'], colors=colors, alpha=0.7)

ax.set_title('Renewable Energy by Decade', fontsize=18, fontweight='normal', pad=10)
ax.set_xlabel('Decade', fontsize=14)
ax.set_ylabel('Units', fontsize=14)

ax.legend(loc='lower right', fontsize=11, title='Energy Type', bbox_to_anchor=(0.5, -0.2))

ax.grid(True, linestyle='-', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.show()