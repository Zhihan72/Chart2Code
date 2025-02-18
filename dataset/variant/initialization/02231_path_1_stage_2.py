import matplotlib.pyplot as plt
import numpy as np

ingredients = ['Dragon Scales', 'Unicorn Horn', 'Phoenix Feathers', 'Mandrake Root', 'Elven Elixir']
potencies = [
    [50, 55, 53, 52, 51, 56, 54, 58, 52, 59],
    [75, 78, 77, 80, 79, 76, 81, 82, 83, 78],
    [65, 68, 70, 67, 66, 69, 71, 72, 65, 68],
    [40, 42, 41, 43, 39, 44, 40, 45, 42, 41],
    [90, 95, 92, 93, 91, 96, 94, 97, 93, 95]
]
average_potencies = [54, 79, 67, 43, 92]

# Shuffle colors by manually reordering the colors from the original list
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']
shuffled_colors = ['lightcoral', 'lightpink', 'lightsalmon', 'lightgreen', 'lightblue']

fig, ax = plt.subplots(figsize=(12, 8))
boxes = ax.boxplot(potencies, patch_artist=True, notch=True, vert=True, showmeans=True)

# Applying the shuffled colors to boxplot elements
for patch, color in zip(boxes['boxes'], shuffled_colors):
    patch.set_facecolor(color)

ax.plot(range(1, len(average_potencies) + 1), average_potencies, 
        marker='s', linestyle='-', color='darkred', linewidth=2)

ax.set_xticks(range(1, len(ingredients) + 1))
ax.set_xticklabels(ingredients, fontsize=10, rotation=15, ha='right')
plt.tight_layout()
plt.show()