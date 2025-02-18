import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia']
sandwich_types_left = ['Club', 'Cuban']  # Assume these are positive direction
sandwich_types_right = ['Grilled Cheese', 'PB&J', 'BLT']  # Assume these are negative direction

# Separate the popularity into two sets for positive and negative sides
popularity_left = np.array([
    [25, 30],
    [15, 20],
    [10, 15]
])

popularity_right = np.array([
    [20, 15, 10],
    [25, 20, 20],
    [30, 25, 20]
])

colors_left = ['#4682B4', '#FF6347']
colors_right = ['#32CD32', '#9400D3', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 8))

# Plot on the left side of the center
bottom_left = np.zeros(len(regions))

for idx, (sandwich, color) in enumerate(zip(sandwich_types_left, colors_left)):
    ax.bar(regions, popularity_left[:, idx], bottom=bottom_left, color=color, label=sandwich, alpha=0.8)
    bottom_left += popularity_left[:, idx]

# Plot on the right side of the center
bottom_right = np.zeros(len(regions))

for idx, (sandwich, color) in enumerate(zip(sandwich_types_right, colors_right)):
    ax.bar(regions, -popularity_right[:, idx], bottom=-bottom_right, color=color, label=sandwich, alpha=0.8)
    bottom_right += popularity_right[:, idx]

ax.set_title("Regional Sandwich Preferences (Diverging)", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Popularity (%)", fontsize=12)
ax.set_xlabel("World Regions", fontsize=12)

plt.xticks(rotation=30, ha='center')

ax.legend(title="Types of Sandwiches", loc='upper center', ncol=3)

ax.yaxis.grid(True, linestyle='--', which='both', color='gray', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()