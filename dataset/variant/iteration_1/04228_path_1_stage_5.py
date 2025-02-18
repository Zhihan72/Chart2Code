import matplotlib.pyplot as plt
import numpy as np

zones = ['Veg', 'Frt', 'Grn', 'Leg', 'Hrb', 'Flw']
zone_acres = np.array([20, 25, 25, 15, 10, 5])

# Manually shuffled colors
colors = ['#fb8072', '#bebada', '#fdb462', '#80b1d3', '#8dd3c7', '#ffffb3']
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    zone_acres,
    explode=explode,
    labels=zones,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

ax.axis('equal')

plt.show()