import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

na_recovery = [2500, 500, 3500, 4500]
eu_recovery = [4500, 600, 5000, 3000]
asia_recovery = [6000, 1200, 9000, 8000]
sa_recovery = [1500, 300, 1000, 2000]
africa_recovery = [800, 1000, 150, 700]

data = np.array([na_recovery, eu_recovery, asia_recovery, sa_recovery, africa_recovery])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#d62728', '#2ca02c', '#ff7f0e', '#1f77b4']

n_datasets = data.shape[1]
bar_positions = np.arange(len(regions))
bar_width = 0.2

for i in range(n_datasets):
    ax.bar(bar_positions + i * bar_width, data[:, i], width=bar_width, color=colors[i], alpha=0.8)

ax.set_xticks(bar_positions + bar_width * (n_datasets - 1) / 2)
ax.set_xticklabels(regions)
ax.set_ylim(0, max(data.max(axis=0)) * 1.1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()

plt.show()