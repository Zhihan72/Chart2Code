import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
lunar_rabbits_population = [50, 52, 58, 65, 70, 68, 75, 72, 71, 79, 80, 84]

fig, ax = plt.subplots(figsize=(10, 6))

color = 'teal'
ax.plot(months, lunar_rabbits_population, marker='^', linestyle='-.', color=color, linewidth=2, markersize=8)

ax.grid(True, linestyle='-', alpha=0.5, color='lightgray')

ax.set_xticks(months)
ax.set_xticklabels(['', '', '', '', '', '', '', '', '', '', '', ''], rotation=45, ha='center')

plt.tight_layout()
plt.show()