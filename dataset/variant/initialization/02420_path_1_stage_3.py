import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
sandwich_types = ['Club', 'Cuban', 'Grilled Cheese', 'PB&J', 'BLT']

popularity = np.array([
    [25, 30, 20, 15, 10],
    [15, 20, 25, 20, 20],
    [10, 15, 30, 25, 20]
])

colors = ['#32CD32', '#FFD700', '#9400D3', '#4682B4', '#FF6347']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = np.zeros(len(regions))

for idx, (sandwich, color) in enumerate(zip(sandwich_types, colors)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8)
    bottom += popularity[:, idx]

ax.set_title("Regional Sandwich Love:\nExploring Global Cravings", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Popularity (%)", fontsize=12)
ax.set_xlabel("World Regions", fontsize=12)

plt.xticks(rotation=45, ha='right')
ax.legend(title="Types of Sandwiches", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()