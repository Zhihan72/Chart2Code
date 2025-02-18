import matplotlib.pyplot as plt
import numpy as np

missions = ["Voyager", "Galileo", "Cassini", "New Horizons", "Rosetta", "Juno", "Crewed Missions"]
discoveries = [15, 22, 30, 10, 8, 13, 6]
discoveries_per_year = np.array(discoveries) / np.array([40, 10, 20, 15, 12, 10, 60])

fig, ax1 = plt.subplots(figsize=(14, 8))
bars = ax1.barh(missions, discoveries, color='steelblue', edgecolor='k')

ax2 = ax1.twiny()
ax2.plot(discoveries_per_year, missions, color='steelblue', marker='o', linestyle='-', linewidth=2, markersize=8)

plt.tight_layout()
plt.show()