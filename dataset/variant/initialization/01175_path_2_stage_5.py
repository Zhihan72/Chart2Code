import matplotlib.pyplot as plt
import numpy as np

quarters = np.array([
    'Q4 2024', 'Q3 2025', 'Q1 2025', 'Q2 2025',
    'Q3 2024', 'Q2 2024', 'Q1 2024', 'Q4 2025'
])

projected_revenues = np.array([165, 218, 200, 192, 175, 150, 160, 212])
errors = np.array([7, 14, 12, 9, 10, 5, 8, 13])

sorted_indices = np.argsort(projected_revenues)
quarters = quarters[sorted_indices]
projected_revenues = projected_revenues[sorted_indices]
errors = errors[sorted_indices]

plt.figure(figsize=(12, 6))
plt.bar(
    quarters, projected_revenues, yerr=errors, capsize=5,
    color=['#1f77b4', '#ff7f0e'], ecolor='black', alpha=0.85
)
plt.title('Surprise Fortune Prospect\nin the Tech Arena', fontsize=16, color='darkgreen', fontweight='bold')
plt.xlabel('Fiscal Time Slot', fontsize=12, color='navy')
plt.ylabel('Estimated Earnings (Million $)', fontsize=12, color='maroon')
plt.xticks(rotation=90, fontsize=10, color='teal')
plt.yticks(fontsize=10, color='teal')
plt.grid(True, linestyle='-', linewidth=0.5, color='grey')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.legend(['Earnings Projection'], loc='upper right')
plt.show()