import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q2 2024', 'Q1 2024', 'Q4 2024', 'Q3 2024',
    'Q2 2025', 'Q1 2025', 'Q4 2025', 'Q3 2025'
])

projected_revenues = np.array([150, 160, 165, 175, 192, 200, 212, 218])
errors = np.array([5, 8, 7, 10, 9, 12, 13, 14])

sorted_indices = np.argsort(projected_revenues)
quarters = quarters[sorted_indices]
projected_revenues = projected_revenues[sorted_indices]
errors = errors[sorted_indices]

plt.figure(figsize=(12, 6))
plt.bar(
    quarters, projected_revenues, yerr=errors, capsize=5,
    color=['#1f77b4', '#ff7f0e'], ecolor='black', alpha=0.85
)
plt.title('Quarterly Revenue Forecast\nin the Tech Industry', fontsize=16, color='navy', fontweight='bold')
plt.xlabel('Quarter', fontsize=12, color='darkred')
plt.ylabel('Revenue (Million $)', fontsize=12, color='darkgreen')
plt.xticks(rotation=90, fontsize=10, color='purple')
plt.yticks(fontsize=10, color='purple')
plt.grid(True, linestyle='-', linewidth=0.5, color='grey')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.legend(['Projected Revenue'], loc='upper left')
plt.show()