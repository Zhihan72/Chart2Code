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

colors = plt.cm.plasma(np.linspace(0, 1, len(labels)))

fig, ax = plt.subplots(figsize=(11, 11), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct=lambda pct: '{:.1f}%\n({:d})'.format(pct, int(np.round(pct/100.*np.sum(sizes)))),
    startangle=140, 
    explode=[0.05]*len(labels)
)

ax.axis('equal')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(10)
    autotext.set_weight('bold')

plt.tight_layout()
plt.show()