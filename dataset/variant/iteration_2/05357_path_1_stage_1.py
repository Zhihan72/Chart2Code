import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

# Artificial data for bird population (in thousands)
sparrows = np.array([15, 16, 14, 13, 12, 19, 21, 17, 14, 15, 23])  # shuffled some elements
robins = np.array([10, 10, 11, 14, 17, 12, 19, 12, 16, 15, 10])    # shuffled some elements
blue_jays = np.array([5, 8, 7, 10, 12, 8, 12, 6, 9, 14, 10])       # shuffled some elements
eagles = np.array([2, 3, 3, 4, 6, 2, 7, 5, 4, 5, 3])               # shuffled some elements

data = np.vstack([sparrows, robins, blue_jays, eagles])

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Sparrows', 'Robins', 'Blue Jays', 'Eagles'],
             colors=['#FFD700', '#FFA07A', '#87CEFA', '#98FB98'], alpha=0.8)

ax.set_title('Bird Population Trends at Sanctuary Wildlife Reserve (2012-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Population (in thousands)', fontsize=14)
ax.legend(loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

milestones = {
    2014: 'Peak in Sparrow Population',
    2018: 'Introduction of New Feeding Programs',
    2022: 'Initiation of Eagle Conservation'
}

for year, event in milestones.items():
    total_population = sparrows[year-2012] + robins[year-2012] + blue_jays[year-2012] + eagles[year-2012]
    ax.annotate(event, xy=(year, total_population/2),
                xytext=(year, total_population/2 + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', backgroundcolor='white')

plt.tight_layout()
plt.show()