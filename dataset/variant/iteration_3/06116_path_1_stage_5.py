import matplotlib.pyplot as plt
import numpy as np

superheroes = ["Captain Plasma", "Mighty Wasp", "Red Cyclone", "Shadow Panther", "Lightning Lynx"]
years = ["2018", "2019", "2020", "2021", "2022"]

rescues = np.array([
    [120, 130, 150, 140, 170],
    [90, 100, 110, 105, 120],
    [80, 85, 95, 100, 110],
    [110, 115, 120, 130, 135],
    [70, 75, 85, 90, 100]
])
battles = np.array([
    [80, 95, 105, 100, 110],
    [60, 70, 80, 75, 85],
    [75, 80, 90, 85, 95],
    [90, 100, 110, 105, 115],
    [65, 70, 75, 80, 85]
])
community = np.array([
    [30, 40, 50, 45, 55],
    [20, 25, 30, 35, 40],
    [25, 30, 35, 40, 45],
    [35, 40, 45, 50, 55],
    [15, 20, 25, 30, 35]
])

fig, axs = plt.subplots(figsize=(12, 8))
width = 0.25
x = np.arange(len(years))

colors = ['#1abc9c', '#e74c3c', '#8e44ad', '#f1c40f', '#3498db']
markers = ['o', '--', '^', ':', '*']

for i in range(len(superheroes)):
    axs.bar(x, rescues[i], width, color=colors[i], edgecolor='black', hatch=markers[i], bottom=battles[i]+community[i])
    axs.bar(x, battles[i], width, color=colors[i], edgecolor='black', bottom=community[i])
    axs.bar(x, community[i], width, color=colors[i], edgecolor='black')
    x = x + width

# axs.set_title('Superhero Missions Overview', fontsize=16, fontweight='bold')
# axs.set_xlabel('Years', fontsize=12)
# axs.set_ylabel('Missions Count', fontsize=12)

axs.set_xticks(np.arange(len(years)) + 2 * width)
# axs.set_xticklabels(years)

# axs.legend(title='Missions Summary', loc='upper right', fontsize=8, frameon=False)
axs.yaxis.grid(True, linestyle=':', alpha=0.5)
axs.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()