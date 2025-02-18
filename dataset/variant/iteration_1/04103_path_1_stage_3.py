import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 101, 10)

distance_to_planets = {
    'Earth': [0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0],
    'Mars': [0, 35, 100, 120, 200, 270, 300, 330, 400, 480, 520],
    'Jupiter': [0, 80, 210, 290, 370, 490, 650, 820, 920, 1080, 1260],
    'Saturn': [0, 130, 290, 470, 620, 700, 960, 1130, 1390, 1510, 1740],
    'Neptune': [0, 210, 380, 590, 810, 1030, 1240, 1490, 1800, 1980, 2240]
}

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['blue', 'orange', 'green', 'purple', 'red']

for idx, (planet, distances) in enumerate(distance_to_planets.items()):
    ax.plot(time, distances, marker='o', linestyle='-', linewidth=2, alpha=0.7, color=colors[idx])

ax.set_title('Voyager X: Journey Across the Solar System', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (Months)', fontsize=12)
ax.set_ylabel('Distance from Earth (Million km)', fontsize=12)

ax.annotate('Mars Mission Completed', xy=(50, 520), xytext=(30, 700),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax.annotate('Jupiter Flyby', xy=(60, 650), xytext=(70, 800),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax.annotate('Saturn Ring Study', xy=(90, 1510), xytext=(50, 1350),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

fig.tight_layout()

plt.show()