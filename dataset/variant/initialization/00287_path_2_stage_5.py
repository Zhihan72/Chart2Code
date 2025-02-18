import matplotlib.pyplot as plt
import numpy as np

dragon_stats = [8, 6, 9, 7, 5]
unicorn_stats = [5, 9, 7, 8, 9]

angles = np.linspace(0, 2 * np.pi, len(dragon_stats), endpoint=False).tolist()
angles += angles[:1]

def plot_creature(ax, stats, color, line_style, marker):
    stats += stats[:1]
    ax.plot(angles, stats, color=color, linestyle=line_style, marker=marker)
    ax.fill(angles, stats, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Changed colors for the plots
plot_creature(ax, dragon_stats, 'darkorange', '--', 'o')
plot_creature(ax, unicorn_stats, 'royalblue', '-.', 's')

plt.xticks(ticks=angles[:-1], labels=['A', 'B', 'C', 'D', 'E'])
ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)
ax.xaxis.grid(True)
ax.yaxis.grid(False)
plt.ylim(0, 10)

plt.tight_layout()
plt.show()