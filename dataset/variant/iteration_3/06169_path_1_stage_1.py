import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Altered e-waste material recovery data (in metric tons)
na_recovery = [4000, 3200, 2700, 600]  # slightly altered
eu_recovery = [5200, 4200, 2900, 700]  # slightly altered
asia_recovery = [8500, 7800, 6200, 1250]  # slightly altered
sa_recovery = [2100, 1400, 1100, 250]  # slightly altered
africa_recovery = [900, 850, 650, 180]  # slightly altered

data = np.array([na_recovery, eu_recovery, asia_recovery, sa_recovery, africa_recovery])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
bar_positions = np.arange(len(regions))
bar_width = 0.6
bottoms = np.zeros(len(regions))

for i in range(data.shape[1]):
    ax.bar(bar_positions, data[:, i], width=bar_width, label=['Metals', 'Plastics', 'Glass', 'Electronics'][i],
           color=colors[i], bottom=bottoms, alpha=0.8)
    bottoms += data[:, i]

ax.set_title('Regional E-Waste Recycling Impact in 2023:\nMaterial Recovery Breakdown', fontsize=16, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Recovered Materials (Metric Tons)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(regions, fontsize=10)
ax.set_ylim(0, max(data.sum(axis=1)) * 1.1)

ax.legend(title='Recovered Material Type', fontsize=10)

for i, region_data in enumerate(data):
    cumulative = 0
    for j, amount in enumerate(region_data):
        ax.text(i, cumulative + amount / 2, f'{amount}', ha='center', va='center', fontsize=9, color='white')
        cumulative += amount

plt.tight_layout()
plt.show()