import matplotlib.pyplot as plt
import numpy as np

years = np.arange(3050, 3055)
exports = {
    'Zerion': [50, 55, 52, 54, 53],
    'Yutopia': [20, 22, 23, 25, 24],
    'Cetheron': [-30, -33, -35, -36, -38],
    'Luthar': [-10, -15, -18, -20, -22],
    'Xanadu': [40, 42, 45, 46, 48],
    'Hyperion': [-25, -28, -30, -32, -34]
}

colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2', '#937860']

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, exports['Zerion'], label='Zerion', color=colors[0])
ax.bar(years, exports['Yutopia'], bottom=exports['Zerion'], label='Yutopia', color=colors[1])
ax.bar(years, exports['Cetheron'], label='Cetheron', color=colors[2], align='center')
ax.bar(years, exports['Luthar'], bottom=exports['Cetheron'], label='Luthar', color=colors[3], align='center')
ax.bar(years, exports['Xanadu'], bottom=[sum(x) for x in zip(exports['Zerion'], exports['Yutopia'])], label='Xanadu', color=colors[4])
ax.bar(years, exports['Hyperion'], bottom=[sum(x) for x in zip(exports['Cetheron'], exports['Luthar'])], label='Hyperion', color=colors[5], align='center')

ax.set_title("Galactic Exports 3050-54", fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Quantity (kTons)", fontsize=12, labelpad=15)

plt.xticks(years, rotation=45)

ax.legend(title='Planets', loc='upper left', bbox_to_anchor=(1, 1.05))

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()