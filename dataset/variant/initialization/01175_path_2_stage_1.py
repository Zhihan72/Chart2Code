import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024',
    'Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025'
])

# Randomly altered projected revenues and error margins while keeping the structure
projected_revenues = np.array([160, 150, 175, 165, 200, 192, 218, 212])
errors = np.array([8, 5, 10, 7, 12, 9, 14, 13])

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
plt.annotate('Projected Peak', xy=('Q3 2025', 218), xytext=('Q1 2025', 225),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
plt.tight_layout()
plt.show()