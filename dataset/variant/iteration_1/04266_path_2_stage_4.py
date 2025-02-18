import matplotlib.pyplot as plt
import numpy as np

# Data
monthly_observations = [
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 9, 10],
    [1, 0, 4, 3, 7, 6, 8, 9, 10, 12, 6, 5],
    # Removed third data group: [7, 8, 10, 6, 5, 4, 9, 10, 11, 12, 6, 7]
    [2, 4, 3, 5, 6, 1, 3, 5, 7, 8, 9, 11],
    [6, 8, 7, 5, 4, 3, 9, 10, 8, 7, 4, 5],
    [4, 2, 3, 7, 9, 6, 5, 8, 7, 6, 8, 9],
    [8, 9, 7, 6, 8, 5, 4, 6, 8, 10, 7, 5],
    [5, 4, 3, 7, 9, 8, 7, 6, 10, 12, 9, 8],
    [2, 3, 1, 5, 6, 4, 3, 5, 6, 7, 8, 7],
    [4, 6, 5, 7, 8, 4, 6, 9, 10, 11, 9, 8]
]

# Consolidate data for the histogram
all_months = np.concatenate(monthly_observations)

# Create a single histogram plot
fig, ax1 = plt.subplots(figsize=(14, 5))

# Histogram
ax1.hist(all_months, bins=12, color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_xticks(np.arange(1, 13))
# Removed line: ax1.set_xticklabels([])
# Removed line: ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Remove borders
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()