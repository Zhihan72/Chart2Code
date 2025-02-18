import matplotlib.pyplot as plt
import numpy as np

missions = ["Voyager", "Galileo", "Cassini", "New Horizons", "Pioneer", "Rosetta", "Juno", "Crewed"]
discoveries = [15, 22, 30, 10, 18, 8, 13, 6]

years_active = np.array([1977, 1989, 1997, 2006, 1973, 2004, 2011, 1961])
discoveries_per_year = np.array(discoveries) / np.array(
    [40, 10, 20, 15, 12, 12, 10, 60])

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.bar(missions, discoveries, color='skyblue', edgecolor='k')

ax1.set_xlabel("Missions", fontsize=14)
ax1.set_ylabel("Discoveries", fontsize=14)
ax1.set_title("Mission Discoveries", fontsize=16, fontweight='bold')

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height),
             ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2 = ax1.twinx()
ax2.plot(missions, discoveries_per_year, color='darkorange', marker='o', linestyle='-', linewidth=2, markersize=8, label='Discoveries/Year')
ax2.set_ylabel('Disc/Year', fontsize=14, color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')
ax2.legend(loc='upper right')

annotations = {
    "Voyager": "Interstellar",
    "Galileo": "Jupiter",
    "Cassini": "Saturn",
    "New Horizons": "Pluto"
}

for mission, label in annotations.items():
    idx = missions.index(mission)
    ax1.annotate(label, (missions[idx], discoveries[idx]), xytext=(0, 10), textcoords='offset points', 
                 arrowprops=dict(arrowstyle='->', color='gray'),
                 ha='center', fontsize=10, color='maroon')

plt.tight_layout()
plt.show()