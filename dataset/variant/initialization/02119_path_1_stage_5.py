import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
fiction = np.array([30, 35, 40, 45, 50, 55])
non_fiction = np.array([20, 22, 25, 27, 30, 32])
sci_fi = np.array([10, 12, 14, 16, 18, 20])
fantasy = np.array([8, 10, 13, 16, 20, 25])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_indices = np.arange(len(years))

# Randomly altering the stylistic elements
ax.bar(x_indices, fiction, width=bar_width, color='skyblue', alpha=0.7, label='Fiction', hatch='o')
ax.bar(x_indices + bar_width, non_fiction, width=bar_width, color='orange', alpha=0.9, label='Non-Fiction', hatch='//')
ax.bar(x_indices + 2 * bar_width, sci_fi, width=bar_width, color='green', alpha=0.6, label='Sci-Fi', hatch='x')
ax.bar(x_indices + 3 * bar_width, fantasy, width=bar_width, color='purple', alpha=0.8, label='Fantasy', hatch='+')

# Adding a legend at a different position
ax.legend(loc='upper left', fontsize=12)

# Randomly decide to display grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.7)
ax.xaxis.grid(False)  # no vertical grid lines

# Altering borders (spines) visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(x_indices + bar_width * 1.5, years)
plt.tight_layout()
plt.show()