import matplotlib.pyplot as plt
import numpy as np

decades = ['1990s', '2000s', '2010s', '2020s']
solar_energy = [5, 15, 50, 120]
wind_energy = [10, 25, 60, 150]
hydroelectric = [100, 120, 150, 160]

energy_data = np.array([solar_energy, wind_energy, hydroelectric])

fig, ax = plt.subplots(figsize=(12, 7))
colors = ['#FFA07A', '#20B2AA', '#87CEEB']

ax.stackplot(decades, energy_data, colors=colors, alpha=0.8)

ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Energy Contribution\n(Arbitrary Units)', fontsize=12)

plt.tight_layout()
plt.show()