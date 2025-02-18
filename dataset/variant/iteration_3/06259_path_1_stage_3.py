import matplotlib.pyplot as plt
import numpy as np

temperatures = [5, 6, 8, 7, 6, 5, 7, 8, 9, 4, 5, 5, 6, 7, 8, 5, 6, 7, 10, 6, 7, 5, 8, 9]

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(temperatures, vert=True, patch_artist=True,
           boxprops=dict(facecolor='lightgreen', color='darkblue', linewidth=2),
           whiskerprops=dict(color='darkblue', linewidth=2),
           capprops=dict(color='darkblue', linewidth=2),
           medianprops=dict(color='orange', linewidth=2),
           flierprops=dict(markerfacecolor='darkblue', marker='^', markersize=8, alpha=0.8))

ax.set_title('Temperature Data Distribution', fontsize=18, fontweight='bold', color='darkgreen')
ax.set_ylabel('Degrees Celsius', fontsize=12, color='darkblue')
ax.yaxis.grid(True, linestyle='-', which='major', color='black', alpha=0.3)

plt.tight_layout()
plt.show()