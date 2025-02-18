import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1975, 2030, 10)
residential_solar = [1, 4, 15, 30, 50, 70]
commercial_solar = [2, 8, 20, 35, 55, 75]
industrial_solar = [0, 2, 8, 20, 40, 65]
agricultural_solar = [0, 1, 3, 10, 20, 35]

area_data = np.vstack([residential_solar, commercial_solar, industrial_solar, agricultural_solar])
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']

fig, ax = plt.subplots(figsize=(8, 8))
fig.suptitle('Growth of Solar Energy Adoption in the U.S. (1975-2025)', fontsize=16, fontweight='bold', y=1.05)

ax.stackplot(decades, area_data, colors=colors, alpha=0.8)
ax.set_title('Percentage of Total Energy Usage (%)', fontsize=14)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 101, 20))
ax.tick_params(axis='x', rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()