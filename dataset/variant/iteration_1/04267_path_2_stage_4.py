import matplotlib.pyplot as plt
import numpy as np

data = [-5, -3, 0, 2, 1, -1, -4, 3, 2, 0, -2, -3, 1, 2, -3, 0, 3, -1, 4, 3, -2, 0, 3, -1, 2, 3, -1, -2, 1, 2, 
        2, 4, 5, 6, 7, 6, 5, 4, 4, 5, 6, 7, 6, 5, 4, 10, 15, 13, 14, 12, 13, 15, 14, 12, 10, 11, 12, 13, 14, 12, 
        -10, -8, -9, -7, -8, -9, -11, -12, -9, -8, -10, -7, -5, -6, -8]

plt.figure(figsize=(9, 5))

parts = plt.violinplot(data, vert=False, showmeans=True, showmedians=False)

for pc in parts['bodies']:
    pc.set_facecolor('#21AA95')  # Changed color for the body
parts['cmeans'].set_color('#D67DE1')  # Changed to mean line color

plt.title('Weekly Temperature Shifts\nDiverse Regions Data', fontsize=14, fontweight='regular')
plt.xlabel('Temperature Variation (°C)', fontsize=10)
plt.yticks([1], ['Combined Regions'], fontsize=8)

plt.grid(visible=False, axis='x')
plt.plot([0], marker='o', markersize=5)  # Added point markers for illustrative purposes
plt.tight_layout()
plt.show()