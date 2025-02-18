import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Population data for marine species (in thousands)
blue_whales = [12, 10, 8, 9, 11, 10, 12, 15, 17, 16, 18, 20, 23, 25, 24, 22, 20, 18, 17, 19, 16]
coral_reefs = [75, 72, 68, 65, 63, 60, 58, 56, 54, 52, 50, 48, 45, 43, 40, 38, 35, 33, 30, 28, 25]
great_white_sharks = [23, 22, 21, 20, 19, 18, 17, 17, 16, 15, 14, 14, 13, 12, 11, 11, 10, 9, 9, 8, 7]
seabirds = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, blue_whales, marker='o', linestyle='-', color='blue')
ax.plot(years, coral_reefs, marker='^', linestyle='-', color='coral')
ax.plot(years, great_white_sharks, marker='s', linestyle='-', color='gray')
ax.plot(years, seabirds, marker='d', linestyle='-', color='purple')

ax.set_title('Impact of Climate Change on Marine Species \nPopulation Trends from 2000 to 2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (in thousands)', fontsize=12)

plt.tight_layout()
plt.show()