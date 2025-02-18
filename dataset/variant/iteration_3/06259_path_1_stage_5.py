import matplotlib.pyplot as plt
import numpy as np

# Data for temperature groups
temperatures_first = [5, 6, 8, 7, 6, 5, 7, 8, 9, 4, 5, 5, 6, 7, 8, 5, 6, 7, 10, 6, 7, 5, 8, 9]
additional_data1 = [3, 4, 6, 7, 5, 3, 6, 6, 8, 3, 5, 4, 3, 6, 7, 4, 5, 6, 8, 5, 5, 3, 7, 8]
additional_data2 = [7, 8, 9, 10, 9, 8, 7, 11, 10, 9, 8, 7, 8, 9, 10, 9, 8, 9, 11, 9, 8, 7, 10, 11]

# Combine all groups
all_data = [temperatures_first, additional_data1, additional_data2]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(all_data, vert=True, patch_artist=True,
           boxprops=dict(facecolor='lightgreen', color='darkblue', linewidth=2),
           whiskerprops=dict(color='darkblue', linewidth=2),
           capprops=dict(color='darkblue', linewidth=2),
           medianprops=dict(color='orange', linewidth=2),
           flierprops=dict(markerfacecolor='darkblue', marker='^', markersize=8, alpha=0.8))

ax.set_title('Temperature Variability', fontsize=18, fontweight='bold', color='darkgreen')
ax.set_ylabel('Celsius', fontsize=12, color='darkblue')
ax.yaxis.grid(True, linestyle='-', which='major', color='black', alpha=0.3)
ax.set_xticklabels(['Set A', 'Set B', 'Set C'])

plt.tight_layout()
plt.show()