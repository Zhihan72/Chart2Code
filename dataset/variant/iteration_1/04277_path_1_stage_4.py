import matplotlib.pyplot as plt
import numpy as np

missions = ["Voyager", "Galileo", "Cassini", "New Horizons", "Pioneer", "Rosetta", "Juno", "Crewed"]
discoveries = [15, 22, 30, 10, 18, 8, 13, 6]

# Sort missions and discoveries in descending order
sorted_indices = np.argsort(discoveries)[::-1]
missions_sorted = [missions[i] for i in sorted_indices]
discoveries_sorted = [discoveries[i] for i in sorted_indices]

colors = ['lightsalmon', 'lightcoral', 'lightgreen', 'skyblue', 'orchid', 'orange', 'lightsteelblue', 'peachpuff']
colors_sorted = [colors[i] for i in sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))
bars = ax1.bar(missions_sorted, discoveries_sorted, color=colors_sorted)

ax1.set_xlabel("Missions", fontsize=14)
ax1.set_ylabel("Discoveries", fontsize=14)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()