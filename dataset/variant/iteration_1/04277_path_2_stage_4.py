import matplotlib.pyplot as plt
import numpy as np

missions = ["Voyager", "Galileo", "Cassini", "New Horizons", "Rosetta", "Juno", "Crewed Missions"]
discoveries = [15, 22, 30, 10, 8, 13, 6]
discoveries_per_year = np.array(discoveries) / np.array([40, 10, 20, 15, 12, 10, 60])

fig, ax1 = plt.subplots(figsize=(14, 8))
bars = ax1.barh(missions, discoveries, color='steelblue', edgecolor='k')

for bar in bars:
    width = bar.get_width()
    ax1.text(width, bar.get_y() + bar.get_height() / 2.0, '%d' % int(width),
             va='center', ha='left', fontsize=10, fontweight='bold')

ax2 = ax1.twiny()
ax2.plot(discoveries_per_year, missions, color='steelblue', marker='o', linestyle='-', linewidth=2, markersize=8)
ax2.set_xlabel('Discoveries per Year', fontsize=14, color='steelblue')
ax2.tick_params(axis='x', labelcolor='steelblue')

plt.tight_layout()
plt.show()