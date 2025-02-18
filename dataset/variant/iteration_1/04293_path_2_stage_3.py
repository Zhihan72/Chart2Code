import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array(['10-20', '21-30', '31-40', '41-50', '51-60', '61-70'])
physical_activity_level = np.array([45, 60, 55, 40, 30, 20])
happiness_index = np.array([70, 85, 80, 65, 50, 40])

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting horizontal bar chart with altered stylistic elements
ax.barh(age_groups, physical_activity_level, color='navajowhite', edgecolor='blue', alpha=0.7, label='Physical Activity Level', hatch='x')
ax.barh(age_groups, -happiness_index, color='lightcoral', edgecolor='blue', alpha=0.7, label='Happiness Index', hatch='//')

ax.set_xlabel('Values', fontsize=13, fontweight='normal', color='darkcyan')
ax.set_ylabel('Age Groups', fontsize=13, fontweight='normal', color='darkcyan')
ax.set_title('Comparison of Physical Activity and Happiness Index\nAcross Different Age Groups', fontsize=15, fontweight='bold', pad=15)

ax.grid(True, linestyle='-', linewidth=0.6, alpha=0.5, color='lightgrey')  # Changed grid linestyle and color

ax.legend(loc='upper left', fontsize=11, frameon=False)  # Changed legend location and style

plt.tight_layout()
plt.show()