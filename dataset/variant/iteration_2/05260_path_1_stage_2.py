import matplotlib.pyplot as plt
import numpy as np

# Data for one cuisine (unchosen order, Italian used for demonstration)
regions = ['NA', 'EU', 'AS', 'SA', 'AF']
italian_cuisine = [80, 85, 70, 60, 50]
colors = '#FF4500'  # Italian cuisine color

fig, ax = plt.subplots(figsize=(14, 8))
positions = np.arange(len(regions))

ax.bar(positions, italian_cuisine, color=colors, edgecolor='grey', alpha=0.8)

ax.set_title("Italian Cuisine Popularity 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Regions", fontsize=14)
ax.set_ylabel("Popularity", fontsize=14)

ax.set_xticks(positions)
ax.set_xticklabels(regions, fontsize=12)

ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.yaxis.set_ticks(np.arange(0, 101, 10))

plt.tight_layout()
plt.show()