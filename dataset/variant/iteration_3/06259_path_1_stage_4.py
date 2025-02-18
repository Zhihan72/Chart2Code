import matplotlib.pyplot as plt
import numpy as np

# Original temperature data
temperatures_group1 = [5, 6, 8, 7, 6, 5, 7, 8, 9, 4, 5, 5, 6, 7, 8, 5, 6, 7, 10, 6, 7, 5, 8, 9]

# New additional made-up data for two more groups
temperatures_group2 = [3, 4, 6, 7, 5, 3, 6, 6, 8, 3, 5, 4, 3, 6, 7, 4, 5, 6, 8, 5, 5, 3, 7, 8]
temperatures_group3 = [7, 8, 9, 10, 9, 8, 7, 11, 10, 9, 8, 7, 8, 9, 10, 9, 8, 9, 11, 9, 8, 7, 10, 11]

# Combine all data
data = [temperatures_group1, temperatures_group2, temperatures_group3]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(data, vert=True, patch_artist=True,
           boxprops=dict(facecolor='lightgreen', color='darkblue', linewidth=2),
           whiskerprops=dict(color='darkblue', linewidth=2),
           capprops=dict(color='darkblue', linewidth=2),
           medianprops=dict(color='orange', linewidth=2),
           flierprops=dict(markerfacecolor='darkblue', marker='^', markersize=8, alpha=0.8))

ax.set_title('Temperature Data Distribution Across Groups', fontsize=18, fontweight='bold', color='darkgreen')
ax.set_ylabel('Degrees Celsius', fontsize=12, color='darkblue')
ax.yaxis.grid(True, linestyle='-', which='major', color='black', alpha=0.3)
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])

plt.tight_layout()
plt.show()