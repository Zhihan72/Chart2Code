import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

na_recovery = [4000, 3200, 2700, 600]
eu_recovery = [5200, 4200, 2900, 700]
asia_recovery = [8500, 7800, 6200, 1250]
sa_recovery = [2100, 1400, 1100, 250]
africa_recovery = [900, 850, 650, 180]

data = np.array([na_recovery, eu_recovery, asia_recovery, sa_recovery, africa_recovery])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728']
bar_positions = np.arange(len(regions))
bar_width = 0.55
bottoms = np.zeros(len(regions))
hatches = ['', '//', 'x', '\\\\']

for i in range(data.shape[1]):
    ax.bar(bar_positions, data[:, i], width=bar_width, color=colors[i], bottom=bottoms,
           alpha=0.9, edgecolor='black', hatch=hatches[i])
    bottoms += data[:, i]

ax.set_xticks(bar_positions)
ax.set_xticklabels([])  # Removed axis labels by setting empty labels
ax.set_yticks([])  # Removed y-axis labels
ax.set_ylim(0, max(data.sum(axis=1)) * 1.2)

ax.legend([], loc='upper right', frameon=False)  # Removed legend by passing an empty list
ax.grid(False)  # Removed grid because they are essentially text markers

plt.tight_layout()
plt.show()