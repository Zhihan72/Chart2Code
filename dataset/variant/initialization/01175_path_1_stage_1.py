import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024',
    'Q1 2025', 'Q2 2025', 'Q3 2025'
])

projected_revenues = np.array([150, 160, 170, 180, 192, 205, 215])

errors = np.array([5, 6, 8, 10, 9, 11, 12])

plt.figure(figsize=(12, 6))

plt.errorbar(
    quarters, projected_revenues, yerr=errors, fmt='-o',
    ecolor='gray', capsize=5, elinewidth=2, markeredgewidth=2,
    color='#1f77b4', label='Projected Revenue'
)

plt.title('Quarterly Revenue Forecast with Confidence Intervals\nin the Tech Industry', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Revenue (Million $)', fontsize=12)

plt.xticks(rotation=45)

plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(loc='upper left', fontsize=10)

plt.tight_layout()

plt.show()