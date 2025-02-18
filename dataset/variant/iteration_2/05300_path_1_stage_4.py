import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

blue_whales = [12, 17, 10, 9, 11, 19, 10, 15, 8, 16, 18, 20, 23, 25, 24, 22, 20, 18, 17, 19, 16]
coral_reefs = [75, 68, 72, 65, 63, 25, 58, 56, 60, 52, 54, 48, 45, 43, 40, 38, 35, 33, 30, 28, 50]
great_white_sharks = [23, 21, 22, 20, 19, 7, 17, 17, 18, 15, 16, 14, 13, 12, 11, 11, 10, 9, 9, 8, 14]
seabirds = [300, 280, 290, 270, 260, 100, 240, 230, 250, 210, 220, 190, 180, 170, 160, 150, 140, 130, 120, 110, 200]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, blue_whales, marker='p', linestyle='--', color='darkorange', label='Ocean Giants')
ax.plot(years, coral_reefs, marker='v', linestyle='-.', color='teal', label='Reef Structures')
ax.plot(years, great_white_sharks, marker='x', linestyle=':', color='magenta', label='Predatory Sharks')
ax.plot(years, seabirds, marker='*', linestyle='-', color='brown', label='Flying Ocean Dwellers')

ax.set_title('Marine Species Population Trends (2000-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (Thousands)', fontsize=12)

ax.legend(loc='lower left', fontsize=10, frameon=False)

ax.grid(False)

plt.tight_layout()

plt.show()