import matplotlib.pyplot as plt
import numpy as np

# Data definition
decades = np.array([1980, 1990, 2000, 2010, 2020])
sea_levels_ny = np.array([0, 12, 22, 35, 48])
sea_levels_la = np.array([0, 10, 20, 32, 50])
sea_levels_miami = np.array([0, 15, 25, 40, 60])
sea_levels_tokyo = np.array([0, 8, 18, 30, 45])
sea_levels_mumbai = np.array([0, 20, 30, 45, 65])

fig, ax = plt.subplots(figsize=(14, 7))

# Plot the data with stylistic alterations
ax.plot(decades, sea_levels_ny, marker='x', linestyle='-', linewidth=1.5)
ax.plot(decades, sea_levels_la, marker='d', linestyle='-.', linewidth=1.5)
ax.plot(decades, sea_levels_miami, marker='h', linestyle=':', linewidth=1.5)
ax.plot(decades, sea_levels_tokyo, marker='<', linestyle='--', linewidth=1.5)
ax.plot(decades, sea_levels_mumbai, marker='p', linestyle='-', linewidth=1.5)

# Alter the grid
ax.grid(True, linestyle='-', alpha=0.3)

# Set ticks
plt.xticks(decades)
plt.yticks(np.arange(0, 71, 10))

# Alter the border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Optimize layout
plt.tight_layout()

plt.show()