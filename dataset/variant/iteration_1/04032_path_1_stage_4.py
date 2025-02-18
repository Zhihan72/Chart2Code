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

bplot = ax.boxplot(box_data, vert=False, patch_artist=True, notch=False,
                   boxprops=dict(facecolor='lightyellow', color='brown'),
                   whiskerprops=dict(color='brown'),
                   capprops=dict(color='brown'),
                   medianprops=dict(color='darkred', linewidth=2),
                   flierprops=dict(markerfacecolor='blue', marker='o', markersize=8, linestyle='none'))

colors = ['#FFD700', '#FF6347', '#8B0000', '#3CB371', '#4682B4', '#FF69B4']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

plt.tight_layout()

plt.show()