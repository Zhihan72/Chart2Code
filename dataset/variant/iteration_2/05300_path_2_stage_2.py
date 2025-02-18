import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Population (in thousands)
blue_whales = [12, 10, 8, 9, 11, 10, 12, 15, 17, 16, 18, 20, 23, 25, 24, 22, 20, 18, 17, 19, 16]
coral_reefs = [75, 72, 68, 65, 63, 60, 58, 56, 54, 52, 50, 48, 45, 43, 40, 38, 35, 33, 30, 28, 25]
great_white_sharks = [23, 22, 21, 20, 19, 18, 17, 17, 16, 15, 14, 14, 13, 12, 11, 11, 10, 9, 9, 8, 7]
seabirds = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, blue_whales, marker='o', linestyle='-', color='blue', label='Blue Whales')
ax.plot(years, coral_reefs, marker='^', linestyle='-', color='coral', label='Coral Reefs')
ax.plot(years, great_white_sharks, marker='s', linestyle='-', color='gray', label='Sharks')
ax.plot(years, seabirds, marker='d', linestyle='-', color='purple', label='Seabirds')

ax.set_title('Marine Species Trends (2000-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Pop. (thousands)', fontsize=12)
ax.legend()

plt.tight_layout()
plt.show()