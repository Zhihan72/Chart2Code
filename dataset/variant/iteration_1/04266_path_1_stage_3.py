import matplotlib.pyplot as plt
import numpy as np

# Data
monthly_observations = [
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 9, 10],
    [1, 0, 4, 3, 7, 6, 8, 9, 10, 12, 6, 5],
    [7, 8, 10, 6, 5, 4, 9, 10, 11, 12, 6, 7],
    [2, 4, 3, 5, 6, 1, 3, 5, 7, 8, 9, 11],
    [4, 2, 3, 7, 9, 6, 5, 8, 7, 6, 8, 9],
    [8, 9, 7, 6, 8, 5, 4, 6, 8, 10, 7, 5],
    [5, 4, 3, 7, 9, 8, 7, 6, 10, 12, 9, 8],
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 8, 7],
    [4, 6, 5, 7, 8, 4, 6, 9, 10, 11, 9, 8]
]

all_months = np.concatenate(monthly_observations)
months = np.arange(1, 13)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

ax1.hist(all_months, bins=12, color='teal', edgecolor='brown', alpha=0.6, linestyle='-.', linewidth=1.5)
ax1.set_xticks(np.arange(1, 13))
ax1.yaxis.grid(True, linestyle=':', which='major', color='purple', alpha=0.7)

years = [2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019, 2020]
marker_styles = ['o', 's', '^', 'D', '*', 'p', 'X', 'v', '<', '>']
for i, (year, observations) in enumerate(zip(years, monthly_observations)):
    ax2.scatter(months + i * 0.1, observations, s=60, alpha=0.6, marker=marker_styles[i % len(marker_styles)])

ax2.set_xticks(np.arange(1, 13))
ax2.yaxis.grid(True, linestyle='-.', which='major', color='orange', alpha=0.55)

plt.tight_layout()
plt.show()