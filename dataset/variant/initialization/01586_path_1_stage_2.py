import matplotlib.pyplot as plt
import numpy as np

# Data for box plot
digital_dreams_times = [25, 30, 45, 60, 40, 55, 70, 50, 65, 35]
soundscapes_times = [15, 20, 18, 22, 17, 19, 25, 20, 21, 16]
light_labyrinths_times = [30, 45, 35, 50, 40, 60, 55, 45, 50, 40]
kinetic_kinetics_times = [10, 15, 20, 25, 15, 18, 22, 20, 19, 17]
virtual_voyages_times = [60, 75, 90, 70, 80, 85, 95, 88, 72, 78]

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

# Create a single subplot for the box plot
fig, ax1 = plt.subplots(figsize=(8, 8))

# Box plot
bp = ax1.boxplot(box_data, vert=False, patch_artist=True, notch=True, whis=1.5)
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightgoldenrodyellow', 'lightpink']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax1.set_title("Zone Engagement", fontsize=13, pad=15)
ax1.set_xlabel("Time (min)", fontsize=12)
ax1.set_yticks(np.arange(1, len(zones) + 1))
ax1.set_yticklabels(zones, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(0, 100)

# Annotations
ax1.annotate('High', xy=(85, 5), xytext=(90, 5.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax1.annotate('Balanced', xy=(45, 3), xytext=(70, 3.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

# Show plot
plt.show()