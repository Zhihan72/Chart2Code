import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
districtA_trees = np.array([500, 550, 620, 700, 750, 800])
districtB_trees = np.array([600, 620, 640, 680, 720, 760])

bar_width = 0.25
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(r1, districtA_trees, color='blue', width=bar_width, edgecolor='grey')
ax.bar(r2, districtB_trees, color='green', width=bar_width, edgecolor='grey')

ax.set_xlabel('Year', fontweight='bold', fontsize=12)
ax.set_ylabel('Number of Trees Planted', fontweight='bold', fontsize=12)
ax.set_title('Annual Number of Trees Planted\nDifferent Districts (2015-2020)', fontweight='bold', fontsize=14)
ax.set_xticks([r + bar_width / 2 for r in range(len(years))])
ax.set_xticklabels(years)

ax.annotate('Green Milestone Reached', xy=(4, 750), xytext=(2, 820),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()