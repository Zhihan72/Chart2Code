import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)
minerals = [20, 25, 23, 30, 28, 35, 40, 38, 45, 42, 50]
tech_devices = [15, 18, 22, 25, 30, 34, 38, 42, 45, 48, 52]
exotic_foods = [10, 12, 12, 13, 15, 15, 16, 17, 18, 20, 22]

trade_volumes = np.vstack([minerals, tech_devices, exotic_foods])
colors = ['#FFD700', '#00BFFF', '#FF69B4']

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, trade_volumes, colors=colors, alpha=0.8)

ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 121, 20))
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()