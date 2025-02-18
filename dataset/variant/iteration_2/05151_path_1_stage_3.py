import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
lunar_rabbits_population = [50, 52, 58, 65, 70, 68, 75, 72, 71, 79, 80, 84]
sun_chameleons_population = [40, 42, 45, 48, 55, 53, 60, 58, 56, 62, 63, 67]

fig, ax = plt.subplots(figsize=(10, 6))

color = 'teal'
ax.plot(months, lunar_rabbits_population, marker='^', linestyle='-.', color=color, linewidth=2, markersize=8)
ax.plot(months, sun_chameleons_population, marker='D', linestyle=':', color=color, linewidth=2, markersize=8)

ax.grid(True, linestyle='-', alpha=0.5, color='lightgray')

# Remove labels, titles and annotations
ax.set_xticks(months)
ax.set_xticklabels(['', '', '', '', '', '', '', '', '', '', '', ''], rotation=45, ha='center')

plt.tight_layout()
plt.show()