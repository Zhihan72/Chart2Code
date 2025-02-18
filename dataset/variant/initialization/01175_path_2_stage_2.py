import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q2 2024', 'Q1 2024', 'Q4 2024', 'Q3 2024',
    'Q2 2025', 'Q1 2025', 'Q4 2025', 'Q3 2025'
])

# Sorted the projected revenues and errors to correspond with the sorted quarters
projected_revenues = np.array([150, 160, 165, 175, 192, 200, 212, 218])
errors = np.array([5, 8, 7, 10, 9, 12, 13, 14])

# Sort indices of projected revenues to sort the data in ascending order
sorted_indices = np.argsort(projected_revenues)
quarters = quarters[sorted_indices]
projected_revenues = projected_revenues[sorted_indices]
errors = errors[sorted_indices]

plt.figure(figsize=(12, 6))
plt.bar(
    quarters, projected_revenues, yerr=errors, capsize=5,
    color='#1f77b4', ecolor='gray', alpha=0.7
)
plt.title('Quarterly Revenue Forecast\nin the Tech Industry', fontsize=16)
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Revenue (Million $)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()