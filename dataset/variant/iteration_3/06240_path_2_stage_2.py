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
    'James Webb Space Telescope',
    'Imaginary Mission - Alpha Centauri',
    'Fictional Endeavor - Andromeda Galaxy'
]

votes = np.array([850, 760, 900, 650, 715, 680, 620, 690, 640, 780, 500, 450])

fig, ax = plt.subplots(figsize=(14, 9))

# New color palette for the missions
new_colors = ['#e6194b', '#3cb44b', '#ffe119', '#f58231', '#911eb4', 
              '#46f0f0', '#f032e6', '#d2f53c', '#fabebe', '#008080', 
              '#e6beff', '#9a6324']

bars = ax.barh(missions, votes, color=new_colors, edgecolor='black', height=0.6)

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
counts = [1, 11]

# New colors for the pie chart
pie_colors = ['#ff9999', '#66b3ff']

ax2.pie(counts, labels=types, colors=pie_colors, autopct='%1.1f%%', startangle=90, counterclock=False)

ax2.set_title('Mission Types Distribution', fontsize=12)

plt.tight_layout()
plt.show()