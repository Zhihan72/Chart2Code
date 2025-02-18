import matplotlib.pyplot as plt
import numpy as np

ingr = ['Dragon', 'Unicorn', 'Mandrake', 'Elven']
potencies = [
    [50, 55, 53, 52, 51, 56, 54, 58, 52, 59],
    [75, 78, 77, 80, 79, 76, 81, 82, 83, 78],
    [40, 42, 41, 43, 39, 44, 40, 45, 42, 41],
    [90, 95, 92, 93, 91, 96, 94, 97, 93, 95]
]
avg_potencies = [54, 79, 43, 92]

colors = ['lightcoral', 'lightpink', 'lightgreen', 'lightblue']

fig, ax = plt.subplots(figsize=(12, 8))
boxes = ax.boxplot(potencies, patch_artist=True, notch=True, vert=True, showmeans=True)

for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)

ax.plot(range(1, len(avg_potencies) + 1), avg_potencies, 
        marker='s', linestyle='-', color='darkred', linewidth=2)

ax.set_xticks(range(1, len(ingr) + 1))
ax.set_xticklabels(ingr, fontsize=10, rotation=15, ha='right')
plt.tight_layout()
plt.show()