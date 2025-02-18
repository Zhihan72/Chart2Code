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

new_colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B']

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, exports['Zerion'], color=new_colors[0])
ax.bar(years, exports['Yutopia'], bottom=exports['Zerion'], color=new_colors[1])
ax.bar(years, exports['Cetheron'], color=new_colors[2], align='center')
ax.bar(years, exports['Luthar'], bottom=exports['Cetheron'], color=new_colors[3], align='center')
ax.bar(years, exports['Xanadu'], bottom=[sum(x) for x in zip(exports['Zerion'], exports['Yutopia'])], color=new_colors[4])
ax.bar(years, exports['Hyperion'], bottom=[sum(x) for x in zip(exports['Cetheron'], exports['Luthar'])], color=new_colors[5], align='center')

ax.set_title("Galactic Exports 3050-54", fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Quantity (kTons)", fontsize=12, labelpad=15)

plt.xticks(years, rotation=45)

plt.tight_layout()
plt.show()