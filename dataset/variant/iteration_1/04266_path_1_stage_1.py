import matplotlib.pyplot as plt
import numpy as np

# Data
years = list(range(2011, 2021))
monthly_observations = [
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 9, 10],
    [1, 0, 4, 3, 7, 6, 8, 9, 10, 12, 6, 5],
    [7, 8, 10, 6, 5, 4, 9, 10, 11, 12, 6, 7],
    [2, 4, 3, 5, 6, 1, 3, 5, 7, 8, 9, 11],
    [6, 8, 7, 5, 4, 3, 9, 10, 8, 7, 4, 5],
    [4, 2, 3, 7, 9, 6, 5, 8, 7, 6, 8, 9],
    [8, 9, 7, 6, 8, 5, 4, 6, 8, 10, 7, 5],
    [5, 4, 3, 7, 9, 8, 7, 6, 10, 12, 9, 8],
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 8, 7],
    [4, 6, 5, 7, 8, 4, 6, 9, 10, 11, 9, 8]
]

all_months = np.concatenate(monthly_observations)
months = np.arange(1, 13)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Histogram with altered styles
ax1.hist(all_months, bins=12, color='teal', edgecolor='brown', alpha=0.6, linestyle='-.', linewidth=1.5)
ax1.set_title("Annual Distribution of Meteor Showers\n(2011-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xticks(np.arange(1, 13))
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax1.yaxis.grid(True, linestyle=':', which='major', color='purple', alpha=0.7)

# Scatter plot with different styles for markers
marker_styles = ['o', 's', '^', 'D', '*', 'p', 'X', 'v', '<', '>']
for i, (year, observations) in enumerate(zip(years, monthly_observations)):
    ax2.scatter(months + i * 0.1, observations, label=f'{year}', s=60, alpha=0.6, marker=marker_styles[i % len(marker_styles)])

ax2.set_title("Meteor Showers Recorded Monthly\nPer Year from 2011 to 2020", fontsize=16, fontweight='bold', pad=20)
ax2.set_xticks(np.arange(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.yaxis.grid(True, linestyle='-.', which='major', color='orange', alpha=0.55)
ax2.legend(title="Year", fontsize=9, title_fontsize='12', loc='lower left', edgecolor='blue', fancybox=True)

plt.tight_layout()
plt.show()