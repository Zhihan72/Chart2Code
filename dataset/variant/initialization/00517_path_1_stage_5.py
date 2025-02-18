import matplotlib.pyplot as plt
import numpy as np

continents = ['Europe', 'Asia', 'North America', 'South America']
sources = ['Solar', 'Wind', 'Hydro']

energy_data = np.array([
    [200, 150, 100],
    [300, 200, 250],
    [250, 220, 180],
    [120, 100, 300]
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_indices = np.arange(len(continents))

for i in range(len(sources)):
    ax.bar(x_indices + i * bar_width, energy_data[:, i], bar_width)

# Remove grid, legend and borders
ax.grid(False)
ax.legend().set_visible(False)
ax.set_frame_on(False)

plt.tight_layout()
plt.show()