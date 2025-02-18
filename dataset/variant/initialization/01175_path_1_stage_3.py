import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q1', 'Q2', 'Q3', 'Q4',
    'Q1', 'Q2', 'Q3'
])

projected_revenues = np.array([150, 160, 170, 180, 192, 205, 215])

errors = np.array([5, 6, 8, 10, 9, 11, 12])

plt.figure(figsize=(12, 6))

# Randomly altering marker, line style, and color
plt.errorbar(
    quarters, projected_revenues, yerr=errors, fmt='--s',
    ecolor='orange', capsize=5, elinewidth=2, markeredgewidth=2,
    color='green', label='Proj. Revenue'
)

plt.title('Revenue Forecast with Confidence Intervals', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Revenue (Million $)', fontsize=12)

plt.xticks(rotation=45)

# Randomly changing the grid style and alpha
plt.grid(True, linestyle='-.', alpha=0.8)

# Randomly changing the legend's location and font size
plt.legend(loc='lower right', fontsize=8)

plt.tight_layout()

plt.show()