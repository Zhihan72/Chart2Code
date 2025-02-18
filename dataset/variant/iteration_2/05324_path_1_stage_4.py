import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

new_york = np.array([32, 35, 65, 55, 60, 75, 80, 70, 50, 78, 45, 30])
los_angeles = np.array([60, 55, 58, 70, 75, 62, 78, 65, 82, 58, 70, 80])
chicago = np.array([28, 30, 45, 50, 60, 73, 65, 70, 25, 75, 40, 55])
houston = np.array([55, 75, 60, 50, 85, 70, 90, 92, 65, 55, 80, 85])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, new_york, marker='x', linestyle='--', markersize=8, linewidth=1.5, color='green')
ax.plot(months, los_angeles, marker='*', linestyle='-', markersize=10, linewidth=2.5, color='orange')
ax.plot(months, chicago, marker='h', linestyle=':', markersize=7, linewidth=1, color='blue')
ax.plot(months, houston, marker='p', linestyle='-.', markersize=9, linewidth=3, color='red')

ax.grid(False)

ax.legend(['New York', 'Los Angeles', 'Chicago', 'Houston'], loc='upper right', frameon=False)

plt.show()