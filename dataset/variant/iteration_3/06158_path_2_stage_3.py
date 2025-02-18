import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Flavor Variety', 'Affordability', 'Customer Service', 'Ambience', 'Quality']
N = len(categories)

# Manually shuffled scores
shopA_scores = [7, 8, 8, 9, 6]
shopB_scores = [6, 9, 7, 8, 8]
shopC_scores = [8, 7, 9, 7, 7]
shopD_scores = [8, 6, 9, 8, 7]

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

shopA_scores += shopA_scores[:1]
shopB_scores += shopB_scores[:1]
shopC_scores += shopC_scores[:1]
shopD_scores += shopD_scores[:1]

def plot_radar(ax, data, color):
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plot_radar(ax, shopA_scores, '#1f77b4')
plot_radar(ax, shopB_scores, '#ff7f0e')
plot_radar(ax, shopC_scores, '#2ca02c')
plot_radar(ax, shopD_scores, '#d62728')

ax.set_ylim(0, 10)
ax.xaxis.grid(False)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

plt.tight_layout()
plt.show()