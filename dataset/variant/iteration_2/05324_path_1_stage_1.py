import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

new_york = np.array([30, 32, 45, 55, 65, 75, 80, 78, 70, 60, 50, 35])
los_angeles = np.array([55, 58, 60, 65, 70, 75, 80, 82, 78, 70, 62, 58])
chicago = np.array([25, 28, 40, 50, 60, 70, 75, 73, 65, 55, 45, 30])
houston = np.array([50, 55, 60, 70, 80, 85, 90, 92, 85, 75, 65, 55])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, new_york, marker='o', linestyle='-', markersize=6, linewidth=2, color='blue')
ax.plot(months, los_angeles, marker='s', linestyle='--', markersize=6, linewidth=2, color='orange')
ax.plot(months, chicago, marker='^', linestyle='-', markersize=6, linewidth=2, color='green')
ax.plot(months, houston, marker='D', linestyle=':', markersize=6, linewidth=2, color='red')

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()