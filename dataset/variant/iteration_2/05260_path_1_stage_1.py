import matplotlib.pyplot as plt
import numpy as np

# Data preparation
regions = ['NA', 'EU', 'AS', 'SA', 'AF']
italian_cuisine = [80, 85, 70, 60, 50]
chinese_cuisine = [75, 70, 90, 55, 60]
mexican_cuisine = [65, 60, 50, 80, 40]
indian_cuisine = [55, 65, 85, 50, 70]

cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian']
data = [italian_cuisine, chinese_cuisine, mexican_cuisine, indian_cuisine]
colors = ['#FF4500', '#228B22', '#4169E1', '#FFD700']

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
positions = np.arange(len(regions))

for i, (cuisine, popularity) in enumerate(zip(cuisines, data)):
    ax.bar(positions + i * bar_width, popularity, width=bar_width,
           color=colors[i], edgecolor='grey', label=cuisine, alpha=0.8)

# Shortened titles and labels
ax.set_title("Cuisine Popularity 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Regions", fontsize=14)
ax.set_ylabel("Popularity", fontsize=14)

ax.set_xticks(positions + bar_width * 1.5)
ax.set_xticklabels(regions, fontsize=12)

ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.yaxis.set_ticks(np.arange(0, 101, 10))

ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1.01, 1), borderaxespad=0.)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()