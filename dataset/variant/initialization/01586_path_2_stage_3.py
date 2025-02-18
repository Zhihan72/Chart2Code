import matplotlib.pyplot as plt
import numpy as np

# Data for box plot including new exhibit
digital_dreams_times = [25, 30, 45, 60, 40, 55, 70, 50, 65, 35]
soundscapes_times = [15, 20, 18, 22, 17, 19, 25, 20, 21, 16]
light_labyrinths_times = [30, 45, 35, 50, 40, 60, 55, 45, 50, 40]
kinetic_kinetics_times = [10, 15, 20, 25, 15, 18, 22, 20, 19, 17]
virtual_voyages_times = [60, 75, 90, 70, 80, 85, 95, 88, 72, 78]
neon_nights_times = [55, 60, 65, 58, 62, 67, 70, 66, 63, 61]

# Combine data including new exhibit
box_data = [
    digital_dreams_times,
    soundscapes_times,
    light_labyrinths_times,
    kinetic_kinetics_times,
    virtual_voyages_times,
    neon_nights_times
]

# Data for the line plot including new exhibit
days = np.arange(1, 11)
avg_times = {
    "Digital Dreams": [45, 47, 50, 48, 46, 51, 52, 49, 53, 50],
    "Soundscapes": [19, 21, 20, 18, 22, 23, 21, 20, 19, 21],
    "Light Labyrinths": [40, 42, 45, 43, 41, 46, 47, 44, 48, 45],
    "Kinetic Kinetics": [17, 18, 20, 19, 17, 21, 20, 18, 19, 18],
    "Virtual Voyages": [80, 82, 85, 84, 81, 86, 88, 85, 87, 84],
    "Neon Nights": [62, 64, 68, 67, 65, 70, 71, 69, 72, 68]
}

# Create a 2x1 subplot layout
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Create horizontal box plot
bp = ax1.boxplot(box_data, vert=False, patch_artist=True, notch=True, whis=1.5)
new_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightcyan', 'lightpink', 'lightgray']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set_facecolor(color)

ax1.set_yticks([])
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(0, 100)

# Create a line plot for average times
for zone, times in avg_times.items():
    ax2.plot(days, times, marker='o')

ax2.set_xticks([])
ax2.set_yticks([])
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend().set_visible(False)

plt.tight_layout()
plt.show()