import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

temperatures_ny = [30, 32, 35, 33, 30, 31, 29]
temperatures_chicago = [20, 22, 25, 24, 22, 21, 19]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(days, temperatures_ny, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)
ax.plot(days, temperatures_chicago, marker='^', linestyle='-.', color='red', linewidth=2, markersize=6)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(np.arange(len(days)))

plt.tight_layout()
plt.show()