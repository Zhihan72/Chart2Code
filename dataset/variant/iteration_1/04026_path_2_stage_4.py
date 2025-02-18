import matplotlib.pyplot as plt
import numpy as np

creatures = ['Dragons', 'Unicorns', 'Phoenixes', 'Mermaids']
popularity = [40, 25, 20, 10]

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
wedges, autotexts = ax.pie(popularity, colors=colors, startangle=90, pctdistance=0.85, explode=[0.2, 0, 0, 0.1])

for pct in autotexts:
    pct.set_fontsize(11)
    pct.set_color('navy')

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.show()