import matplotlib.pyplot as plt
import numpy as np

age_groups = np.array(['10-20', '21-30', '31-40', '41-50', '51-60', '61-70'])
physical_activity_level = np.array([45, 60, 55, 40, 30, 20])
happiness_index = np.array([70, 85, 80, 65, 50, 40])

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting horizontal bar chart
ax.barh(age_groups, physical_activity_level, color='lightblue', edgecolor='black', alpha=0.8, label='Physical Activity Level')
ax.barh(age_groups, -happiness_index, color='salmon', edgecolor='black', alpha=0.8, label='Happiness Index')

ax.set_xlabel('Values', fontsize=14, fontweight='semibold')
ax.set_ylabel('Age Groups', fontsize=14, fontweight='semibold')
ax.set_title('Comparison of Physical Activity and Happiness Index\nAcross Different Age Groups', fontsize=16, fontweight='bold', pad=20)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='grey')

ax.legend(loc='lower right', fontsize=12, frameon=True)

plt.tight_layout()
plt.show()