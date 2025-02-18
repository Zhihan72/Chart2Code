import matplotlib.pyplot as plt
import numpy as np

# Data for crop yields (in kg) over three seasons: spring, summer, and autumn
tomato_yields = [
    [12, 15, 14, 13, 12, 16, 17, 19, 14, 15],  # Spring
    [22, 24, 23, 25, 22, 28, 29, 26, 24, 23],  # Summer
    [18, 19, 20, 17, 19, 18, 21, 22, 20, 18]   # Autumn
]

carrot_yields = [
    [5, 6, 5.5, 6.2, 6.5, 5.8, 6.3, 5, 5.5, 6],  # Spring
    [7, 7.5, 8, 7.8, 7.5, 7.2, 8.5, 8, 7.7, 8.2], # Summer
    [10, 9.8, 10.2, 9.5, 10, 10.1, 9.7, 10.3, 10.5, 9.9]  # Autumn
]

lettuce_yields = [
    [4, 3.8, 4.2, 4.1, 4, 3.9, 4.3, 3.7, 4.4, 3.8],  # Spring
    [5, 4.8, 4.9, 5.2, 4.9, 4.7, 5.3, 5, 5.1, 4.8],  # Summer
    [6, 5.8, 6.1, 5.9, 6, 5.7, 6.2, 5.9, 6.3, 6.1]   # Autumn
]

data = [tomato_yields, carrot_yields, lettuce_yields]
seasons = ["Spring", "Summer", "Autumn"]
common_color = '#FFA07A'  # Single color for all data groups

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
positions = np.array(range(len(seasons))) * 4

# Horizontal Box Plot
for i, yields in enumerate(data):
    pos = positions + i
    bp = axes[0].boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=False, vert=False)
    for patch in bp['boxes']:
        patch.set_facecolor(common_color)
    for whisker in bp['whiskers']:
        whisker.set(color='brown', linestyle='-.', linewidth=1)
    for cap in bp['caps']:
        cap.set(color='brown', linestyle='-.', linewidth=1)
    for median in bp['medians']:
        median.set(color='blue', linewidth=1.5, linestyle='-.')

axes[0].set_yticks(positions + 1)
axes[0].grid(axis='x', linestyle=':', alpha=0.5)

# Line Plot for average yields
seasonal_averages = {
    'Spring': [
        np.mean(tomato_yields[0]),
        np.mean(carrot_yields[0]),
        np.mean(lettuce_yields[0])
    ],
    'Summer': [
        np.mean(tomato_yields[1]),
        np.mean(carrot_yields[1]),
        np.mean(lettuce_yields[1])
    ],
    'Autumn': [
        np.mean(tomato_yields[2]),
        np.mean(carrot_yields[2]),
        np.mean(lettuce_yields[2])
    ]
}

x_pos = np.arange(len(seasons))
average_values = [
    [season[0] for season in seasonal_averages.values()],  # Tomatoes
    [season[1] for season in seasonal_averages.values()],  # Carrots
    [season[2] for season in seasonal_averages.values()]   # Lettuce
]

for i in range(len(data)):
    axes[1].plot(x_pos, average_values[i], marker='s', linestyle='--', linewidth=2, markersize=10, color=common_color)

axes[1].set_xticks(x_pos)
axes[1].grid(axis='both', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()