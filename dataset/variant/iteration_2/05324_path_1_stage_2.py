import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Randomly altered data values while preserving dimensional structure
new_york = np.array([32, 35, 65, 55, 60, 75, 80, 70, 50, 78, 45, 30])
los_angeles = np.array([60, 55, 58, 70, 75, 62, 78, 65, 82, 58, 70, 80])
chicago = np.array([28, 30, 45, 50, 60, 73, 65, 70, 25, 75, 40, 55])
houston = np.array([55, 75, 60, 50, 85, 70, 90, 92, 65, 55, 80, 85])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, new_york, marker='o', linestyle='-', markersize=6, linewidth=2, color='blue')
ax.plot(months, los_angeles, marker='s', linestyle='--', markersize=6, linewidth=2, color='orange')
ax.plot(months, chicago, marker='^', linestyle='-', markersize=6, linewidth=2, color='green')
ax.plot(months, houston, marker='D', linestyle=':', markersize=6, linewidth=2, color='red')

ax.grid(True, linestyle='--', alpha=0.7)

plt.show()