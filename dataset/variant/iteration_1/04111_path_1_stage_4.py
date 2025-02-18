import matplotlib.pyplot as plt
import numpy as np

cities = ['Sydney', 'Paris', 'New York', 'Tokyo', 'London']
cuisines = ['Italian', 'Chinese', 'Indian', 'French']

data = np.array([
    [80, 75, 60, 95],
    [90, 85, 70, 100],
    [120, 90, 60, 75],
    [85, 95, 110, 90],
    [100, 110, 95, 80]
])

sums = data.sum(axis=1)
sorted_indices = np.argsort(sums)

cities = [cities[i] for i in sorted_indices]
data = data[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
r = np.arange(len(cities))
colors = ['purple', 'orange', 'cyan', 'green']

for i in range(len(cuisines)):
    ax.bar(r + i * bar_width, data[:, i], width=bar_width, color=colors[i], edgecolor='grey')

ax.set_xticks(r + 1.5 * bar_width)
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

plt.tight_layout()
plt.show()