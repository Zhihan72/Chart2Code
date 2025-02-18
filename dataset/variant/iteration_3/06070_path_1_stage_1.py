import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
japan_speeds = [130, 200, 240, 270, 300, 320, 350]
france_speeds = [120, 160, 200, 270, 300, 320, 330]
germany_speeds = [100, 150, 200, 250, 280, 300, 320]
china_speeds = [0, 0, 0, 200, 250, 300, 350]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(decades, japan_speeds, marker='o', linestyle='-', linewidth=2, color='red')
ax.plot(decades, france_speeds, marker='s', linestyle='--', linewidth=2, color='blue')
ax.plot(decades, germany_speeds, marker='^', linestyle='-.', linewidth=2, color='green')
ax.plot(decades, china_speeds, marker='d', linestyle=':', linewidth=2, color='purple')

ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 401, 50))

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()