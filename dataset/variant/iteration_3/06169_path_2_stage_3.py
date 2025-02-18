import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Data for each region
na_recovery = [2500, 500, 3500, 4500]
eu_recovery = [4500, 600, 5000, 3000]
asia_recovery = [6000, 1200, 9000, 8000]
sa_recovery = [1500, 300, 1000, 2000]
africa_recovery = [800, 1000, 150, 700]

data = np.array([na_recovery, eu_recovery, asia_recovery, sa_recovery, africa_recovery])

fig, ax = plt.subplots(figsize=(14, 8))

# Manually shuffled colors
colors = ['#d62728', '#2ca02c', '#ff7f0e', '#1f77b4']

bar_positions = np.arange(len(regions))
bar_width = 0.6

bottoms = np.zeros(len(regions))

# Plot bars
for i in range(data.shape[1]):
    ax.bar(bar_positions, data[:, i], width=bar_width, color=colors[i], bottom=bottoms, alpha=0.8)
    bottoms += data[:, i]

ax.set_xticks(bar_positions)

ax.set_ylim(0, max(data.sum(axis=1)) * 1.1)

plt.tight_layout()

plt.show()