import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

sparrows = np.array([15, 14, 13, 12, 14, 15, 16, 17, 19, 21, 23])
robins = np.array([10, 12, 11, 10, 10, 12, 14, 15, 16, 17, 19])
blue_jays = np.array([5, 6, 7, 8, 8, 9, 10, 10, 12, 12, 14])
eagles = np.array([2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7])

data = np.vstack([sparrows, robins, blue_jays, eagles])

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Feathered Friends', 'Winged Wonders', 'Sky Dancers', 'Majestic Gliders'],
             colors=['#98FB98', '#87CEFA', '#FFD700', '#FFA07A'], alpha=0.8)

ax.set_title('Avian Abundance at Enchanted Forest (2012-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Count (thousands)', fontsize=14)

ax.legend(loc='upper left', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

milestones = {
    2014: 'High Sparrow Census',
    2018: 'Start of New Programs',
    2022: 'Eagle Protection Kickoff'
}

for year, event in milestones.items():
    total_population = sparrows[year-2012] + robins[year-2012] + blue_jays[year-2012] + eagles[year-2012]
    ax.annotate(event, xy=(year, total_population/2),
                xytext=(year, total_population/2 + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', backgroundcolor='white')

plt.tight_layout()
plt.show()