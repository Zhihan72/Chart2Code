import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
sandwich_types = ['Club', 'Cuban', 'Grilled Cheese', 'PB&J', 'BLT']

popularity = np.array([
    [25, 30, 20, 15, 10],
    [15, 20, 25, 20, 20],
    [10, 15, 30, 25, 20]
])

# Altered colors, added hatch patterns, changed legend placement
colors = ['#4682B4', '#FF6347', '#32CD32', '#9400D3', '#FFD700']
hatches = ['/', '\\', '|', '-', '+']

fig, ax = plt.subplots(figsize=(12, 8))

bottom = np.zeros(len(regions))

for idx, (sandwich, color, hatch) in enumerate(zip(sandwich_types, colors, hatches)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8, hatch=hatch)
    bottom += popularity[:, idx]

ax.set_title("Regional Sandwich Love:\nExploring Global Cravings", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Popularity (%)", fontsize=12)
ax.set_xlabel("World Regions", fontsize=12)

# Changed x-tick rotation alignment
plt.xticks(rotation=30, ha='center')

# Changed legend properties
ax.legend(title="Types of Sandwiches", loc='upper center', ncol=3)

# Added gridlines and changed border visibility
ax.yaxis.grid(True, linestyle='--', which='both', color='gray', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()