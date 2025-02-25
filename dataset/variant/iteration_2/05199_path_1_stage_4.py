import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
batteries = [0.5, 1, 2, 4, 6, 10, 15, 22, 30, 40, 52]
pumped_storage = [5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]
compressed_air = [0.2, 0.3, 0.5, 0.9, 1.2, 1.5, 2, 2.5, 3, 3.5, 4]

storage_data = np.array([batteries, pumped_storage, compressed_air])
colors = ['#66B2FF', '#FF6F61', '#6B5B95']

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, storage_data, labels=["Batt", "Pump-Stor", "Comp-Air"], 
             colors=colors, alpha=0.8)

ax.set_title("Storage 2015-2025", fontsize=14, fontweight='medium', pad=25)
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Capacity (GWh)", fontsize=11)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 90)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)} GWh'))

ax.legend(loc='upper right', title="Type", fontsize=9, frameon=True, shadow=True)
ax.grid(axis='y', linestyle='-.', alpha=0.5)

for spine in ax.spines.values():
    spine.set_linewidth(1.5)
    spine.set_linestyle('-.')

plt.tight_layout()
plt.show()