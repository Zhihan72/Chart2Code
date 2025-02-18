import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Population (in thousands) - manually shuffled within the same data groups
blue_whales = [10, 11, 8, 12, 15, 12, 10, 18, 9, 16, 20, 23, 17, 22, 19, 25, 24, 18, 17, 19, 16]
coral_reefs = [72, 63, 68, 75, 60, 56, 58, 54, 65, 52, 48, 40, 45, 33, 30, 38, 50, 43, 35, 28, 25]
great_white_sharks = [22, 19, 18, 21, 17, 16, 15, 20, 14, 14, 13, 12, 11, 9, 10, 8, 7, 23, 11, 9, 17]
seabirds = [290, 270, 260, 280, 230, 220, 210, 250, 190, 200, 180, 170, 150, 140, 160, 120, 300, 110, 130, 100, 240]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, blue_whales, marker='o', linestyle='-', color='purple', label='Blue Whales')
ax.plot(years, coral_reefs, marker='^', linestyle='-', color='gray', label='Coral Reefs')
ax.plot(years, great_white_sharks, marker='s', linestyle='-', color='coral', label='Sharks')
ax.plot(years, seabirds, marker='d', linestyle='-', color='blue', label='Seabirds')

ax.set_title('Marine Species Trends (2000-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Pop. (thousands)', fontsize=12)
ax.legend()

plt.tight_layout()
plt.show()