import matplotlib.pyplot as plt
import numpy as np

publishers = ['Pub A', 'Pub B', 'Pub C']
genres = ['Fiction', 'NonFiction', 'SciFi', 'Fantasy', 'History']

data = np.array([
    [120, 150, 80, 100, 90],     
    [200, 180, 170, 160, 140],   
    [90, 130, 110, 95, 85]
])

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5
positions = np.arange(len(genres))

colors = ['#FF9999', '#66B3FF', '#99FF99']

center_positions = np.zeros(len(genres))

for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    deviation = data[idx] - np.mean(data, axis=0)
    ax.barh(positions, deviation, bar_width, left=center_positions, 
            label=publisher, color=color, alpha=0.75)
    center_positions += deviation

ax.set_yticks(positions)
ax.set_yticklabels(genres)
ax.set_xlabel('Deviation from Average Publications', fontsize=12)
ax.set_ylabel('Genres', fontsize=12)
ax.set_title('Diverging Publications by Genres', fontsize=14, fontweight='bold')
ax.axvline(0, color='black', linewidth=0.8)
ax.legend()

plt.tight_layout()
plt.show()