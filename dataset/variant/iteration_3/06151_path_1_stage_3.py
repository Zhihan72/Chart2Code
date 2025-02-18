import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
districtA_trees = np.array([500, 550, 620, 700, 750, 800])
districtB_trees = np.array([600, 620, 640, 680, 720, 760])

bar_height = 0.25
r1 = np.arange(len(years))
r2 = [x + bar_height for x in r1]

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(r1, districtA_trees, color='blue', height=bar_height, edgecolor='grey')
ax.barh(r2, districtB_trees, color='green', height=bar_height, edgecolor='grey')

ax.set_ylabel('Year', fontweight='bold', fontsize=12)
ax.set_xlabel('Number of Trees Planted', fontweight='bold', fontsize=12)
ax.set_title('Annual Number of Trees Planted\nDifferent Districts (2015-2020)', fontweight='bold', fontsize=14)
ax.set_yticks([r + bar_height / 2 for r in range(len(years))])
ax.set_yticklabels(years)

ax.annotate('Green Milestone Reached', xy=(750, 4), xytext=(820, 2),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()