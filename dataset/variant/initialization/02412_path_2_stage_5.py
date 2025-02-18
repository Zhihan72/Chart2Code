import numpy as np
import matplotlib.pyplot as plt

years = np.array(['50', '51', '52', '53', '54'])
destinations = ['Moon', 'Mars', 'Orbit']

tourists_data = np.array([
    [40, 20, 35, 30, 25],
    [10, 15, 22, 30, 5],
    [28, 36, 15, 20, 45],
])

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#4daf4a', '#e41a1c', '#377eb8']
bar_width = 0.2

for idx, (destination, color) in enumerate(zip(destinations, colors)):
    y_pos = np.arange(len(years)) + idx * bar_width
    ax.barh(y_pos, tourists_data[idx], height=bar_width, color=color,
            edgecolor='grey', linewidth=0.5, label=destination)

ax.set_yticks(np.arange(len(years)) + bar_width)
ax.set_yticklabels(years)
ax.set_xlabel('Tourists')
ax.set_ylabel('Year')
ax.set_title('Space Tourism (2050-54)', pad=20, fontsize=14, weight='bold')
ax.legend(title='Destinations', loc='best', fontsize=8)

ax.grid(True, linestyle='-', color='lightgrey', linewidth=0.7, axis='x')

plt.tight_layout()
plt.show()