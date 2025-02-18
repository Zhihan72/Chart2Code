import matplotlib.pyplot as plt
import numpy as np

chocolate_brands = ["CocoaHeaven", "ChocoDelight", "SweetCocoa", "DarkFantasy", "ChocoTwist", "NuttyBites"]

chocolate_data = {
    "CocoaHeaven": [75, 80, 78, 85, 82],
    "ChocoDelight": [70, 75, 72, 78, 79],
    "SweetCocoa": [68, 72, 70, 74, 69],
    "DarkFantasy": [80, 85, 83, 88, 86],
    "ChocoTwist": [65, 67, 66, 70, 68],
    "NuttyBites": [72, 77, 75, 79, 76]
}

box_data = [list(year_data) for year_data in zip(*chocolate_data.values())]

fig, ax = plt.subplots(figsize=(10, 6))

color = '#4682B4'  # Consistent single color for all elements

bplot = ax.boxplot(box_data, vert=False, patch_artist=True, notch=False,
                   boxprops=dict(facecolor=color, color=color),
                   whiskerprops=dict(color=color),
                   capprops=dict(color=color),
                   medianprops=dict(color=color, linewidth=2),
                   flierprops=dict(markerfacecolor=color, marker='o', markersize=8, linestyle='none'))

plt.tight_layout()

plt.show()