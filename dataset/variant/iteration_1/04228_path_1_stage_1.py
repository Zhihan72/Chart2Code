import matplotlib.pyplot as plt
import numpy as np

# Data: Cultivation zone distribution
zones = ['Veg', 'Frt', 'Grn', 'Leg', 'Hrb', 'Flw']
zone_acres = np.array([25, 20, 30, 15, 5, 5])

colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']

# Emphasize the 'Grains' slice
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    zone_acres,
    explode=explode,
    labels=zones,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title('GreenEarth Farming Zones', fontsize=16, weight='bold', pad=20)

ax.legend(wedges, zones, title="Zones", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()

plt.show()