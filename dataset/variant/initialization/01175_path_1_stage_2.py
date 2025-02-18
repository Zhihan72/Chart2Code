import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q1', 'Q2', 'Q3', 'Q4',
    'Q1', 'Q2', 'Q3'
])

projected_revenues = np.array([150, 160, 170, 180, 192, 205, 215])

errors = np.array([5, 6, 8, 10, 9, 11, 12])

plt.figure(figsize=(12, 6))

plt.errorbar(
    quarters, projected_revenues, yerr=errors, fmt='-o',
    ecolor='gray', capsize=5, elinewidth=2, markeredgewidth=2,
    color='#1f77b4', label='Proj. Rev.'
)

plt.title('Revenue Forecast with Confidence Intervals', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Rev. (M $)', fontsize=12)

plt.xticks(rotation=45)

plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(loc='upper left', fontsize=10)

plt.tight_layout()

plt.show()