import matplotlib.pyplot as plt
import numpy as np

missions = [
    'Moon Landing - Apollo 11',
    'Mars Rover - Curiosity',
    'International Space Station (ISS)',
    'Voyager Probes',
    'Hubble Space Telescope',
    'SpaceX Falcon 9 Launch',
    'Rosetta Comet Mission',
    'New Horizons Pluto Flyby',
    'Galileo Jupiter Mission',
    'James Webb Space Telescope'
]

votes = np.array([850, 760, 900, 650, 715, 680, 620, 690, 640, 780])

fig, ax = plt.subplots(figsize=(14, 9))

# Manually shuffled color palette
shuffled_colors = [
    (0.993248, 0.906157, 0.143936, 1.0),  # Yellowish part of viridis
    (0.127568, 0.566949, 0.550556, 1.0),  # Teal part of viridis
    (0.993248, 0.906157, 0.143936, 1.0),  # Yellowish part appears more than once
    (0.267004, 0.004874, 0.329415, 1.0),  # Purple part of viridis
    (0.26851, 0.009605, 0.335427, 1.0),   # Slightly different purple
    (0.993248, 0.906157, 0.143936, 1.0),  # Yellowish part appears more than once
    (0.127568, 0.566949, 0.550556, 1.0),  # Teal part appears more than once
    (0.993248, 0.906157, 0.143936, 1.0),  # Yellowish part appears more than once
    (0.280267, 0.165302, 0.470647, 1.0),  # Dark blue part of viridis
    (0.127568, 0.566949, 0.550556, 1.0)   # Teal part appears more than once
]

bars = ax.barh(missions, votes, color=shuffled_colors, edgecolor='black', height=0.6)

ax.set_title("Global Popularity of Space Exploration Missions\n(Votes in Thousands)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Votes (Thousands)', fontsize=12)
ax.set_ylabel('Missions', fontsize=12)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width}', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

ax.invert_yaxis()
ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='gray')

fig.subplots_adjust(right=0.7)
ax2 = fig.add_axes([0.75, 0.2, 0.25, 0.6])

types = ['Manned', 'Unmanned']
counts = [1, 9]

ax2.pie(counts, labels=types, colors=['#1f77b4', '#ff7f0e'], autopct='%1.1f%%', startangle=90, counterclock=False)
ax2.set_title('Mission Types Distribution', fontsize=12)

plt.tight_layout()

plt.show()