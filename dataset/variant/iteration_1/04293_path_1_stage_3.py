import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array(['20-30', '31-40', '41-50', '51-60', '10-20'])
physical_activity_level = np.array([45, 60, 55, 40, 30])

# Shuffling the happiness_index manually
# Original: [70, 85, 80, 65, 50]
happiness_index = np.array([80, 50, 70, 85, 65])

fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(physical_activity_level, happiness_index, c=happiness_index, cmap='plasma', s=150, edgecolor='black', alpha=0.8)

for i, age in enumerate(age_groups):
    ax.annotate(age, (physical_activity_level[i] + 0.5, happiness_index[i] + 1.5), fontsize=9, ha='center')

coefficients = np.polyfit(physical_activity_level, happiness_index, 1)
poly_eqn = np.poly1d(coefficients)
trendline = poly_eqn(physical_activity_level)
ax.plot(physical_activity_level, trendline, linestyle='--', color='blue', linewidth=2, label=f'Trend Line: {coefficients[0]:.2f}x + {coefficients[1]:.2f}')

ax.set_xlabel('Activity Minutes Per Day', fontsize=14, fontweight='semibold')
ax.set_ylabel('Happiness Rate (Max 100)', fontsize=14, fontweight='semibold')
ax.set_title('Analysis of Activity and Happiness\nGrouped by Ages', fontsize=16, fontweight='bold', pad=20)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='grey')

cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Happiness Scale', rotation=270, labelpad=20, fontsize=12)

ax.legend(loc='lower right', fontsize=12, frameon=True)

plt.tight_layout()
plt.show()