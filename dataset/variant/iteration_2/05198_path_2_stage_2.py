import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2023)

elves = np.array([1.4, 3.7, 1.9, 1.9, 3.8, 1.7, 1, 1.4, 2.4, 2.7, 3.1, 3.9, 3.2, 3.5, 2.1, 4, 1.1, 1.5, 2.5, 2.3, 3.3, 1.35, 1.2])
dwarfs = np.array([1.65, 1.7, 1.3, 2.3, 2.1, 1.25, 1.75, 1.99, 2.05, 1.5, 1.4, 2.02, 1.2, 1.92, 1.45, 1.55, 2.15, 1.95, 1.35, 2.1, 1.88, 1.82, 2.2])
humans = np.array([4.4, 5.4, 6.6, 5.2, 6.2, 4.2, 6.8, 4.6, 5.6, 5.8, 3.2, 3, 6, 4.4, 4.8, 5, 7, 4, 6.4, 6, 3.1, 3.4, 3.2])
orcs = np.array([2, 3.6, 0.65, 2.4, 3.4, 3.2, 2.2, 0.5, 1.4, 0.7, 1, 0.9, 1.6, 1.8, 3, 2.6, 1.2, 3.5, 3.3, 3.1, 2.8, 0.55, 0.6])
fairies = np.array([0.44, 0.64, 0.52, 0.48, 0.68, 0.5, 0.32, 0.35, 0.62, 0.6, 0.46, 0.3, 0.7, 0.36, 0.55, 0.66, 0.53, 0.42, 0.72, 0.58, 0.31, 0.4, 0.33])

population_data = np.vstack([elves, dwarfs, humans, orcs, fairies])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, population_data,
             colors=['#FF9999', '#FFB266', '#8FB266', '#4D7399', '#E066FF'], alpha=0.8)

ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(years[0], years[-1])
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45, ha='right')

plt.tight_layout()
plt.show()