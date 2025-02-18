import matplotlib.pyplot as plt
import numpy as np

data = [-5, -3, 0, 2, 1, -1, -4, 3, 2, 0, -2, -3, 1, 2, -3, 0, 3, -1, 4, 3, -2, 0, 3, -1, 2, 3, -1, -2, 1, 2, 
        2, 4, 5, 6, 7, 6, 5, 4, 4, 5, 6, 7, 6, 5, 4, 10, 15, 13, 14, 12, 13, 15, 14, 12, 10, 11, 12, 13, 14, 12, 
        -10, -8, -9, -7, -8, -9, -11, -12, -9, -8, -10, -7, -5, -6, -8]

plt.figure(figsize=(8, 6))

parts = plt.violinplot(data, vert=False, showmeans=False, showmedians=True)

# Change colors for the violin plot
for pc in parts['bodies']:
    pc.set_facecolor('#2E86C1')  # Set a specific color for the body
parts['cmedians'].set_color('#E74C3C')  # Change median line color

plt.title('Weekly Temperature Shifts\nMixed Locations Data', fontsize=16, fontweight='bold')
plt.xlabel('Temperature Variations (°C)', fontsize=12)
plt.yticks([1], ['All Cities Grouped'], fontsize=10)

plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()