import matplotlib.pyplot as plt
import numpy as np

species_count = [90, 12, 150, 45, 25, 15]
colors = ['#ff6f69', '#ffcc5c', '#88d8b0', '#4d648d', '#8b4513', '#ffb6c1']  # New set of colors
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, _ = ax.pie(species_count, labels=None, autopct=None, startangle=140,
                                  colors=colors, explode=explode, pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.show()