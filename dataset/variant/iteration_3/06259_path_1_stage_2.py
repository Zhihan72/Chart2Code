import matplotlib.pyplot as plt
import numpy as np

temperatures = [5, 6, 8, 7, 6, 5, 7, 8, 9, 4, 5, 5, 6, 7, 8, 5, 6, 7, 10, 6, 7, 5, 8, 9]

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(temperatures, vert=True, patch_artist=True,
           boxprops=dict(facecolor='lightblue', color='chocolate', linewidth=1.5),
           whiskerprops=dict(color='chocolate', linewidth=1.5),
           capprops=dict(color='chocolate', linewidth=1.5),
           medianprops=dict(color='red', linewidth=1.5),
           flierprops=dict(markerfacecolor='chocolate', marker='o', markersize=6, alpha=0.6))

ax.set_title('Box Plot of Temperature Data', fontsize=16, fontweight='bold')
ax.set_ylabel('Temperature (Celsius)', fontsize=14)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()