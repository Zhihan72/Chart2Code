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

fig.tight_layout()

plt.show()