import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2061)

moon = np.array([0, 2, 5, 7, 10, 14, 18, 21, 25, 28, 30, 32, 35, 37, 40, 42, 45, 48, 50, 52, 55])
mars = np.array([0, 0, 1, 3, 6, 10, 14, 17, 20, 24, 28, 31, 34, 37, 40, 43, 46, 49, 52, 56, 60])
europa = np.array([0, 0, 0, 1, 3, 5, 8, 11, 14, 17, 20, 22, 24, 26, 30, 33, 35, 37, 40, 43, 45])
titan = np.array([0, 0, 0, 0, 1, 2, 3, 5, 7, 10, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25])

data = np.vstack([moon, mars, europa, titan])

colors = ['#4682B4', '#32CD32', '#DAA520', '#FF6347']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, colors=colors, alpha=0.85)

ax.grid(False)

total_settlements = moon + mars + europa + titan
perc_moon = 100 * moon / total_settlements
perc_mars = 100 * mars / total_settlements
perc_europa = 100 * europa / total_settlements
perc_titan = 100 * titan / total_settlements

ax2 = ax.twinx()
ax2.plot(years, perc_moon, '^-.', color='#4682B4')
ax2.plot(years, perc_mars, '^-.', color='#32CD32')
ax2.plot(years, perc_europa, '^-.', color='#DAA520')
ax2.plot(years, perc_titan, '^-.', color='#FF6347')
ax2.set_ylim(0, 100)

plt.tight_layout()

plt.show()