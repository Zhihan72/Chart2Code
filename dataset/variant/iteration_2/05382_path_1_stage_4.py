import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
residential_production = np.array([1, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114])
commercial_production = np.array([2, 2, 3, 4, 6, 8, 11, 14, 18, 23, 29, 36, 44, 53, 63, 74, 86, 99, 113, 128, 144])
industrial_production = np.array([1, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210])
community_production = np.array([0, 1, 1, 2, 3, 4, 5, 7, 9, 12, 16, 21, 27, 34, 42, 51, 61, 72, 84, 97, 111])

production_data = np.vstack([residential_production, commercial_production, industrial_production, community_production])

fig, ax = plt.subplots(figsize=(14, 8))

color = '#4682B4'

ax.stackplot(years, production_data, colors=[color]*4, alpha=0.5)

ax.set_xticks(years[::5])
ax.set_yticks(np.arange(0, 501, 100))
ax.yaxis.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()