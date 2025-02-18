import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)
minerals = [20, 25, 23, 30, 28, 35, 40, 38, 45, 42, 50]
tech_devices = [15, 18, 22, 25, 30, 34, 38, 42, 45, 48, 52]

trade_volumes = np.vstack([minerals, tech_devices])
colors = ['#FF5733', '#C70039']  # Different colors for data groups

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, trade_volumes, colors=colors, alpha=0.8)

# Modify legend
ax.legend(['Minerals', 'Tech Devices'], loc='lower right', fontsize=12, bbox_to_anchor=(1, 0.1), frameon=False)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 25))

# Change grid style
ax.grid(True, linestyle='-.', color='gray', linewidth=0.5)

# Remove the top and right borders (spines)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()