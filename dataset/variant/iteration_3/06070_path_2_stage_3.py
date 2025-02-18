import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Randomly altered data within original dimensional structure
japan_speeds = [200, 240, 130, 320, 270, 300, 350]
france_speeds = [160, 300, 120, 330, 200, 270, 320]
germany_speeds = [250, 100, 300, 320, 280, 200, 150]
china_speeds = [0, 350, 0, 200, 0, 250, 300]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(decades, japan_speeds, marker='o', linestyle='-', linewidth=2, color='red')
ax.plot(decades, france_speeds, marker='s', linestyle='--', linewidth=2, color='blue')
ax.plot(decades, germany_speeds, marker='^', linestyle='-.', linewidth=2, color='green')
ax.plot(decades, china_speeds, marker='d', linestyle=':', linewidth=2, color='purple')

ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 401, 50))

plt.tight_layout()
plt.show()