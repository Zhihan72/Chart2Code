import matplotlib.pyplot as plt
import numpy as np

missions = [
    'Lunar Journey - The Eagle',
    'Martian Trek - Explorer',
    'Space Hub (Orbital Outpost)',
    'Galactic Travelers',
    'NextGen Launch Platform',
    'Distant Worlds Voyager',
    'Jovian Odyssey',
]

votes = np.array([850, 760, 900, 650, 680, 690, 640])

fig, ax = plt.subplots(figsize=(14, 9))

shuffled_colors = [
    (0.280267, 0.165302, 0.470647, 1.0),
    (0.127568, 0.566949, 0.550556, 1.0),
    (0.26851, 0.009605, 0.335427, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0),
    (0.267004, 0.004874, 0.329415, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0),
    (0.127568, 0.566949, 0.550556, 1.0)
]

bars = ax.barh(missions, votes, color=shuffled_colors, edgecolor='gray', height=0.6, linestyle='-.')

ax.set_title("Galactic Fame of Space Travel Ventures\n(Opinion Poll Results in 1000s)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Votes (K)', fontsize=12)
ax.set_ylabel('Explorations', fontsize=12)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, f'{width}', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

ax.invert_yaxis()
ax.xaxis.grid(True, linestyle='-.', alpha=0.6, color='darkgray')

fig.subplots_adjust(right=0.7)
ax2 = fig.add_axes([0.75, 0.2, 0.25, 0.6])

types = ['Human-Crewed', 'Machine-Only']
counts = [1, 6]  # Adjusted the count here to reflect the change of data

ax2.pie(counts, labels=types, colors=['#ff7f0e', '#1f77b4'], autopct='%1.1f%%', startangle=270, counterclock=True)
ax2.set_title('Travel Modalities Breakdown', fontsize=12)

plt.tight_layout()
plt.show()