import matplotlib.pyplot as plt
import numpy as np

superheroes = ["Captain Plasma", "Mighty Wasp", "Red Cyclone", "Shadow Panther"]
years = ["2018", "2019", "2020", "2021", "2022"]

rescues = np.array([
    [120, 130, 150, 140, 170],
    [90, 100, 110, 105, 120],
    [80, 85, 95, 100, 110],
    [110, 115, 120, 130, 135]
])
battles = np.array([
    [80, 95, 105, 100, 110],
    [60, 70, 80, 75, 85],
    [75, 80, 90, 85, 95],
    [90, 100, 110, 105, 115]
])
community = np.array([
    [30, 40, 50, 45, 55],
    [20, 25, 30, 35, 40],
    [25, 30, 35, 40, 45],
    [35, 40, 45, 50, 55]
])

fig, axs = plt.subplots(figsize=(12, 7))
width = 0.25
x = np.arange(len(years))

colors = ['#1abc9c', '#e74c3c', '#8e44ad', '#f1c40f']

# New line style shuffle with markers for each superhero
markers = ['o', '--', '^', ':']

for i, hero in enumerate(superheroes):
    axs.bar(x, rescues[i], width, label=f'{hero} - Rescues', color=colors[i], edgecolor='black', hatch=markers[i], bottom=battles[i]+community[i])
    axs.bar(x, battles[i], width, label=f'{hero} - Battles', color=colors[i], edgecolor='black', bottom=community[i])
    axs.bar(x, community[i], width, label=f'{hero} - Community Engagements', color=colors[i], edgecolor='black')
    x = x + width

axs.set_title('Superhero Missions Overview', fontsize=16, fontweight='bold')
axs.set_xlabel('Years', fontsize=12)
axs.set_ylabel('Missions Count', fontsize=12)

axs.set_xticks(np.arange(len(years)) + 1.5 * width)
axs.set_xticklabels(years)

# Randomly altered legend
axs.legend(title='Missions Summary', loc='upper right', fontsize=8, frameon=False)

# Randomly altered grid style
axs.yaxis.grid(True, linestyle=':', alpha=0.5)

# Set spine visibility (random choice)
axs.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()