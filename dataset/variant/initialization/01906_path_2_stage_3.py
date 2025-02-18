import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)
minerals = [20, 25, 23, 30, 28, 35, 40, 38, 45, 42, 50]
tech_devices = [15, 18, 22, 25, 30, 34, 38, 42, 45, 48, 52]

trade_volumes = np.vstack([minerals, tech_devices])
color = '#00BFFF'  # Single consistent color for all data groups

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, trade_volumes, colors=[color, color], alpha=0.8)

ax.legend(['Minerals', 'Tech Devices'], loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 20))
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()