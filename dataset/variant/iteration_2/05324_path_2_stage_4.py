import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
new_york = np.array([30, 32, 45, 55, 65, 75, 80, 78, 70, 60, 50, 35])
los_angeles = np.array([55, 58, 60, 65, 70, 75, 80, 82, 78, 70, 62, 58])
chicago = np.array([25, 28, 40, 50, 60, 70, 75, 73, 65, 55, 45, 30])
houston = np.array([50, 55, 60, 70, 80, 85, 90, 92, 85, 75, 65, 55])
miami = np.array([60, 62, 68, 72, 78, 85, 88, 87, 83, 77, 68, 62])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, new_york, marker='X', linestyle='-', markersize=8, linewidth=1.5, color='blue')
ax.plot(months, los_angeles, marker='*', linestyle='-', markersize=10, linewidth=2.5, color='purple')
ax.plot(months, chicago, marker='h', linestyle='--', markersize=7, linewidth=2, color='red')
ax.plot(months, houston, marker='v', linestyle=':', markersize=8, linewidth=3, color='green')
ax.plot(months, miami, marker='D', linestyle='-.', markersize=6, linewidth=2, color='orange')

# Removed title, labels, legend, and annotations

ax.grid(True, linestyle='-', alpha=0.5, color='gray')
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_visible(False)

plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()