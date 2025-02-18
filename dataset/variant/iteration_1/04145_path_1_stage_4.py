import matplotlib.pyplot as plt
import numpy as np

tomato_yields = [[13, 14, 12, 15, 16, 15, 12, 17, 19, 14],
                 [24, 23, 22, 26, 25, 23, 29, 22, 28, 24],
                 [19, 18, 18, 20, 21, 17, 22, 20, 18, 19]]

carrot_yields = [[6.5, 6, 5, 5.5, 6, 5.8, 5, 6.2, 6.3, 5.5],
                 [7.7, 7.5, 8, 7.2, 8.5, 8, 7, 7.8, 8.2, 7.5],
                 [10.3, 9.8, 10, 9.5, 10.1, 10.2, 10, 10.5, 9.7, 9.9]]

lettuce_yields = [[4.2, 4.1, 3.9, 4.3, 3.8, 4.4, 4, 4, 3.7, 3.8],
                  [4.8, 5.2, 5.3, 4.9, 5.1, 4.8, 5, 4.9, 5, 4.7],
                  [6.2, 6, 5.8, 6.3, 5.9, 6.1, 5.9, 6, 6.1, 5.7]]

seasonal_averages = {
    'Spring': [np.mean(tomato_yields[0]), np.mean(carrot_yields[0]), np.mean(lettuce_yields[0])],
    'Summer': [np.mean(tomato_yields[1]), np.mean(carrot_yields[1]), np.mean(lettuce_yields[1])],
    'Autumn': [np.mean(tomato_yields[2]), np.mean(carrot_yields[2]), np.mean(lettuce_yields[2])],
}

data = [tomato_yields, carrot_yields, lettuce_yields]
# Manually shuffled colors
colors = ['#FFA500', '#98FB98', '#FF6347']
fig, axes = plt.subplots(1, 2, figsize=(20, 10))
positions = np.array(range(3)) * 4

for i, yields in enumerate(data):
    pos = positions + i
    bp = axes[0].boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=True)
    for patch, color in zip(bp['boxes'], [colors[i]] * 3):
        patch.set_facecolor(color)

x_pos = np.arange(3)
average_values = [
    [season[0] for season in seasonal_averages.values()],
    [season[1] for season in seasonal_averages.values()],
    [season[2] for season in seasonal_averages.values()]
]

for i in range(3):
    axes[1].plot(x_pos, average_values[i], marker='o', linestyle='-', linewidth=2, markersize=8, color=colors[i])

plt.tight_layout()
plt.show()