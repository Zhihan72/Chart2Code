import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 101, 10)

distance_to_planets = {
    'Earth': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Mars': [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    'Jupiter': [0, 100, 200, 300, 400, 500, 650, 800, 950, 1100, 1250],
    'Saturn': [0, 150, 300, 450, 600, 750, 950, 1150, 1350, 1550, 1750],
    'Neptune': [0, 200, 400, 600, 800, 1000, 1250, 1500, 1750, 2000, 2250]
}

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['blue', 'orange', 'green', 'purple', 'red']

for idx, (planet, distances) in enumerate(distance_to_planets.items()):
    ax.plot(time, distances, marker='o', linestyle='-', linewidth=2, alpha=0.7, color=colors[idx])

ax.set_title('Voyager X: Journey Across the Solar System', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (Months)', fontsize=12)
ax.set_ylabel('Distance from Earth (Million km)', fontsize=12)

ax.annotate('Mars Mission Completed', xy=(50, 500), xytext=(30, 700),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax.annotate('Jupiter Flyby', xy=(60, 650), xytext=(70, 800),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax.annotate('Saturn Ring Study', xy=(80, 1150), xytext=(50, 1350),
            arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

fig.tight_layout()

plt.show()