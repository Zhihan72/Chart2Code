import matplotlib.pyplot as plt
import numpy as np
from math import pi

dragon_stats = [8, 6, 9, 7, 5]
unicorn_stats = [5, 9, 7, 8, 9]

angles = np.linspace(0, 2 * np.pi, 5, endpoint=False).tolist()
angles += angles[:1]

def plot_creature(ax, stats, color):
    stats += stats[:1]
    ax.plot(angles, stats, color=color, linewidth=2)
    ax.fill(angles, stats, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plot_creature(ax, dragon_stats, 'firebrick')
plot_creature(ax, unicorn_stats, 'forestgreen')

plt.xticks([])
ax.set_rlabel_position(30)
plt.yticks([])
plt.ylim(0, 10)

plt.tight_layout()
plt.show()