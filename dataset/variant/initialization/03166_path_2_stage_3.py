import matplotlib.pyplot as plt
import numpy as np

countries = ['Finland', 'Sweden', 'Brazil', 'Iceland', 'Denmark', 
             'Switzerland', 'Germany', 'Norway', 'USA', 'Italy']
consumption = np.array([12.0, 10.5, 5.0, 9.0, 8.5, 7.9, 6.5, 9.8, 4.5, 4.0])

color_map = plt.get_cmap("YlGnBu")
colors = color_map(np.linspace(0.3, 0.9, len(countries)))

colors_shuffled = [
    colors[3], colors[6], colors[8], colors[1], colors[0], 
    colors[4], colors[2], colors[9], colors[5], colors[7]
]

fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(countries, consumption, color=colors_shuffled, height=0.6)

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Remove grid, title, and axis labels for this task
ax.xaxis.grid(False)
ax.set_title('')
ax.set_xlabel('')
ax.set_ylabel('')

plt.tight_layout()
plt.show()