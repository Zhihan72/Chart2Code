import matplotlib.pyplot as plt
import numpy as np

# Data for box plot
box_data = [
    [25, 30, 45, 60, 40, 55, 70, 50, 65, 35],
    [15, 20, 18, 22, 17, 19, 25, 20, 21, 16],
    [30, 45, 35, 50, 40, 60, 55, 45, 50, 40],
    [10, 15, 20, 25, 15, 18, 22, 20, 19, 17],
    [60, 75, 90, 70, 80, 85, 95, 88, 72, 78],
    [55, 60, 65, 58, 62, 67, 70, 66, 63, 61],
]

days = np.arange(1, 11)
avg_times = {
    "Digital Dreams": [45, 47, 50, 48, 46, 51, 52, 49, 53, 50],
    "Soundscapes": [19, 21, 20, 18, 22, 23, 21, 20, 19, 21],
    "Light Labyrinths": [40, 42, 45, 43, 41, 46, 47, 44, 48, 45],
    "Kinetic Kinetics": [17, 18, 20, 19, 17, 21, 20, 18, 19, 18],
    "Virtual Voyages": [80, 82, 85, 84, 81, 86, 88, 85, 87, 84],
    "Neon Nights": [62, 64, 68, 67, 65, 70, 71, 69, 72, 68],
}

# Create subplots
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 16))

# Create vertical box plot
bp = ax1.boxplot(box_data, vert=True, patch_artist=True, notch=False, whis=1.5)
new_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightcyan', 'lightpink', 'lightgray']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set_facecolor(color)

ax1.set_xticks([])
ax1.set_yticks([])
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_ylim(0, 100)

# Create line plot for average times
for zone, times in avg_times.items():
    ax2.plot(days, times, marker='o')

ax2.set_xticks([])
ax2.set_yticks([])
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend().set_visible(False)

plt.tight_layout()
plt.show()