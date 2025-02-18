import matplotlib.pyplot as plt
import numpy as np

data = {
    'Mars': {'Green': -150, 'Water': 100, 'Energy': -300, 'Med': 50},
    'Luna': {'Green': -100, 'Water': 80, 'Energy': -200, 'Med': 40},
    'Titan': {'Green': -80, 'Water': 60, 'Energy': -150, 'Med': 30},
    'Europa': {'Green': -40, 'Water': 30, 'Energy': -100, 'Med': 20},
    'Ganymede': {'Green': -90, 'Water': 70, 'Energy': -180, 'Med': 35}
}

planets = list(data.keys())
amenities = list(data['Mars'].keys())
values = np.array([[data[planet][amenity] for amenity in amenities] for planet in planets])

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935']
for i, amenity in enumerate(amenities):
    ax.barh(planets, values[:, i], color=colors[i % len(colors)], edgecolor='white')

ax.axvline(0, color='gray', linewidth=0.8)

plt.show()