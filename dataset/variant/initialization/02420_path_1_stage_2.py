import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
sandwich_types = ['PB&J', 'BLT', 'Club', 'Cuban', 'Grilled Cheese']

popularity = np.array([
    [25, 30, 20, 15, 10],
    [15, 20, 25, 20, 20],
    [10, 15, 30, 25, 20]
])

# Shuffled colors for each sandwich type
colors = ['#32CD32', '#FFD700', '#9400D3', '#4682B4', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = np.zeros(len(regions))

for idx, (sandwich, color) in enumerate(zip(sandwich_types, colors)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8)
    bottom += popularity[:, idx]

ax.set_title("Global Appetite for Sandwiches:\nA Stacked Analysis of Regional Preferences", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Popularity Percentage (%)", fontsize=12)
ax.set_xlabel("Regions", fontsize=12)

plt.xticks(rotation=45, ha='right')
ax.legend(title="Sandwich Types", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()