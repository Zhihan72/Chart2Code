import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2061)

moon = np.array([0, 2, 5, 7, 10, 14, 18, 21, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55])
mars = np.array([0, 0, 1, 3, 6, 10, 14, 17, 20, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 56, 60])
europa = np.array([0, 0, 0, 1, 3, 5, 8, 11, 14, 17, 20, 22, 24, 26, 30, 33, 35, 37, 40, 43, 45])

data = np.vstack([moon, mars, europa])

consistent_color = '#4682B4'

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, colors=[consistent_color], alpha=0.85)

ax.grid(False)

# Calculate percentages for remaining datasets
total_settlements = moon + mars + europa
perc_moon = 100 * moon / total_settlements
perc_mars = 100 * mars / total_settlements
perc_europa = 100 * europa / total_settlements

ax2 = ax.twinx()
ax2.plot(years, perc_moon, '^-.', color=consistent_color)
ax2.plot(years, perc_mars, '^-.', color=consistent_color)
ax2.plot(years, perc_europa, '^-.', color=consistent_color)
ax2.set_ylim(0, 100)

plt.tight_layout()

plt.show()