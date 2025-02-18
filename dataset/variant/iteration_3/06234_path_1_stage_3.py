import matplotlib.pyplot as plt
import numpy as np

species_count = [90, 12, 150, 45, 25, 15]
colors = ['#d4a0a7', '#c79efc', '#f0a6ca', '#a6e1fa', '#ceed99', '#f5d76e']
explode = (0, 0, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, _ = ax.pie(species_count, labels=None, autopct=None, startangle=140,
                                  colors=colors, explode=explode, pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.show()