import matplotlib.pyplot as plt
import numpy as np

# Altered Data for box plot
digital_dreams_times = [35, 70, 60, 45, 25, 50, 40, 30, 65, 55]  # shuffled 
soundscapes_times = [22, 20, 15, 19, 18, 21, 17, 20, 16, 25]    # shuffled 
light_labyrinths_times = [40, 50, 60, 35, 40, 45, 55, 30, 50, 45]  # shuffled
kinetic_kinetics_times = [17, 15, 22, 19, 10, 20, 25, 15, 20, 18]   # shuffled
virtual_voyages_times = [72, 95, 90, 80, 70, 78, 88, 85, 60, 75]   # shuffled

box_data = [
    digital_dreams_times,
    soundscapes_times,
    light_labyrinths_times,
    kinetic_kinetics_times,
    virtual_voyages_times
]

zones = [
    "Digital",
    "Sound",
    "Light",
    "Kinetic",
    "Virtual"
]

fig, ax1 = plt.subplots(figsize=(8, 8))
bp = ax1.boxplot(box_data, vert=True, patch_artist=True, notch=True, whis=1.5)
single_color = 'skyblue'
for patch in bp['boxes']:
    patch.set_facecolor(single_color)

ax1.set_title("Zone Engagement", fontsize=13, pad=15)
ax1.set_ylabel("Time (min)", fontsize=12)
ax1.set_xticks(np.arange(1, len(zones) + 1))
ax1.set_xticklabels(zones, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_ylim(0, 100)

ax1.annotate('High', xy=(5, 85), xytext=(5.5, 90),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax1.annotate('Balanced', xy=(3, 45), xytext=(3.5, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

plt.show()