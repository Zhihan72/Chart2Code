import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2050, 2061)

minerals = [20, 25, 23, 30, 28, 35, 40, 38, 45, 42, 50]
tech_devices = [15, 18, 22, 25, 30, 34, 38, 42, 45, 48, 52]
exotic_foods = [10, 12, 12, 13, 15, 15, 16, 17, 18, 20, 22]

trade_volumes = np.vstack([minerals, tech_devices, exotic_foods])

colors = ['#FF69B4', '#FFD700', '#00BFFF']

fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, trade_volumes, labels=['Tech', 'Exotic', 'Minerals'], colors=colors, alpha=0.8)

ax.set_title("Galactic Commerce: 2050-60", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Volume (M Units)", fontsize=12)

ax.legend(loc='upper right', fontsize=10)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 121, 20))

ax.grid(True, linestyle='-.', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()