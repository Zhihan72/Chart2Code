import matplotlib.pyplot as plt
import numpy as np

retreats = ['Mars', 'Jupiter', 'Saturn']
intellectual_diversity = np.array([80, 60, 85])

# Shuffle the colors assigned to each data group
colors = ['coral', 'mediumseagreen', 'royalblue']

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(retreats, intellectual_diversity, color=colors)

ax.set_title("Intellectual Diversity of Galactic Writers' Retreats", fontsize=14, fontweight='bold')
ax.set_xlabel('Intellectual Diversity', fontsize=12)

plt.show()