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

# Flattening and constructing data
all_months = np.concatenate(monthly_observations)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Subplot 1: Histogram
ax1.hist(all_months, bins=12, color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_xticks(np.arange(1, 13))
ax1.set_xticklabels([])
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Subplot 2: Scatter plot
for i, (_, observations) in enumerate(zip(years, monthly_observations)):
    months = np.arange(1, 13) + i * 0.1
    ax2.scatter(months, observations, s=50, alpha=0.7)

ax2.set_xticks(np.arange(1, 13))
ax2.set_xticklabels([])
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
ax2.legend(title=None, fontsize=10, loc='upper right', edgecolor='black', frameon=False)

plt.tight_layout()
plt.show()