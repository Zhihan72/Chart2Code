import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array(['10-20', '21-30', '31-40', '41-50', '51-60'])
physical_activity_level = np.array([45, 60, 55, 40, 30])
happiness_index = np.array([70, 85, 80, 65, 50])

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(age_groups, physical_activity_level, color='navajowhite', edgecolor='blue', alpha=0.7, label='Activity', hatch='x')
ax.barh(age_groups, -happiness_index, color='lightcoral', edgecolor='blue', alpha=0.7, label='Happiness', hatch='//')

ax.set_xlabel('Level', fontsize=13, color='darkcyan')
ax.set_ylabel('Age', fontsize=13, color='darkcyan')
ax.set_title('Physical Activity vs Happiness', fontsize=15, fontweight='bold', pad=15)

ax.grid(True, linestyle='-', linewidth=0.6, alpha=0.5, color='lightgrey')

ax.legend(loc='upper left', fontsize=11, frameon=False)

plt.tight_layout()
plt.show()