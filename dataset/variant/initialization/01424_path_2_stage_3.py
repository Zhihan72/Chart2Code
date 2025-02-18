import matplotlib.pyplot as plt
import numpy as np

# Define the data
labels = [
    'Smart Thermostats', 'Smart Speakers', 'Smart LED Bulbs', 
    'Smart RGB Strips', 'Smart Security Cameras', 'Smart Door Locks', 
    'Smart Smoke Detectors', 'Smart Refrigerators', 'Smart Ovens', 
    'Smart Washing Machines', 'Smart Irrigation Systems', 'Smart Vacuums',
    'Smart Blinds', 'Smart Plugs', 'Smart Air Purifiers'
]
sizes = [8, 10, 7, 5, 15, 6, 4, 9, 7, 8, 6, 15, 5, 6, 8]

# New color set applied from plasma colormap
colors = plt.cm.plasma(np.linspace(0, 1, len(labels)))

fig, ax = plt.subplots(figsize=(11, 11), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct=lambda pct: '{:.1f}%\n({:d})'.format(pct, int(np.round(pct/100.*np.sum(sizes)))),
    startangle=140, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3), 
    explode=[0.05]*len(labels)
)

center_circle = plt.Circle((0, 0), 0.55, fc='white')
fig.gca().add_artist(center_circle)

ax.axis('equal')

plt.title('Dynamic Integration of Advanced Home Technologies\n(A Global Insight)', fontsize=14, fontweight='bold', y=1.08)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(10)
    autotext.set_weight('bold')

ax.legend(wedges, labels, title="Innovations", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.tight_layout()
plt.show()