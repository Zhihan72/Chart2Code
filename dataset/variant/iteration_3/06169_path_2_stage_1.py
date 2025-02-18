import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

na_recovery = [4500, 3500, 2500, 500]
eu_recovery = [5000, 4500, 3000, 600]
asia_recovery = [9000, 8000, 6000, 1200]
sa_recovery = [2000, 1500, 1000, 300]
africa_recovery = [1000, 800, 700, 150]

data = np.array([na_recovery, eu_recovery, asia_recovery, sa_recovery, africa_recovery])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

bar_positions = np.arange(len(regions))
bar_width = 0.6

bottoms = np.zeros(len(regions))

for i in range(data.shape[1]):
    ax.bar(bar_positions, data[:, i], width=bar_width, color=colors[i], bottom=bottoms, alpha=0.8)
    bottoms += data[:, i]

ax.set_xticks(bar_positions)

ax.set_ylim(0, max(data.sum(axis=1)) * 1.1)

plt.tight_layout()

plt.show()