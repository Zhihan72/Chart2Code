import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
gallery_visitors = {
    'New York': [950, 920, 970, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1400],
    'Paris': [750, 780, 760, 800, 850, 880, 910, 930, 950, 970, 1000],
    'Tokyo': [600, 620, 650, 670, 700, 730, 750, 770, 800, 830, 860],
    'London': [890, 870, 880, 920, 940, 960, 1000, 1020, 1040, 1060, 1100]
}

cumulative_visitors = np.sum(list(gallery_visitors.values()), axis=0)

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#D2691E', '#8A2BE2', '#5F9EA0', '#006400']

for (city, visitors), color in zip(gallery_visitors.items(), colors):
    ax1.plot(years, visitors, linestyle='-', color=color, linewidth=2, alpha=0.9)

ax2 = ax1.twinx()
ax2.fill_between(years, 0, cumulative_visitors, color='slategray', alpha=0.3)
ax2.spines['right'].set_color('darkred')
ax2.set_ylim(0, np.max(cumulative_visitors) + 500)

ax1.grid(True, which='major', axis='both', linestyle='-', linewidth=0.7, alpha=0.5)

plt.tight_layout()
plt.show()