import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Manually shuffled population data for marine species (in thousands)
blue_whales = [12, 17, 10, 9, 11, 19, 10, 15, 8, 16, 18, 20, 23, 25, 24, 22, 20, 18, 17, 19, 16]
coral_reefs = [75, 68, 72, 65, 63, 25, 58, 56, 60, 52, 54, 48, 45, 43, 40, 38, 35, 33, 30, 28, 50]
great_white_sharks = [23, 21, 22, 20, 19, 7, 17, 17, 18, 15, 16, 14, 13, 12, 11, 11, 10, 9, 9, 8, 14]
seabirds = [300, 280, 290, 270, 260, 100, 240, 230, 250, 210, 220, 190, 180, 170, 160, 150, 140, 130, 120, 110, 200]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, blue_whales, marker='o', linestyle='-', color='blue', label='Blue Whales')
ax.plot(years, coral_reefs, marker='^', linestyle='-', color='coral', label='Coral Reefs')
ax.plot(years, great_white_sharks, marker='s', linestyle='-', color='gray', label='Great White Sharks')
ax.plot(years, seabirds, marker='d', linestyle='-', color='purple', label='Seabirds')

ax.set_title('Impact of Climate Change on Marine Species \nPopulation Trends from 2000 to 2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (in thousands)', fontsize=12)

ax.legend(loc='upper right', fontsize=10, frameon=True)

ax.annotate('Coral Bleaching Event', xy=(2010, 50), xytext=(2005, 70),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=11, color='red')

ax.annotate('Decline Due to Pollution', xy=(2016, 10), xytext=(2012, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=11, color='red')

ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)

plt.tight_layout()

plt.show()