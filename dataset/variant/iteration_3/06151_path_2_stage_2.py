import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
districtA_trees = np.array([500, 550, 620, 700, 750, 800])
districtB_trees = np.array([600, 620, 640, 680, 720, 760])
districtC_trees = np.array([450, 480, 520, 560, 590, 620])

bar_width = 0.25
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(r1, districtA_trees, color='blue', height=bar_width, edgecolor='grey', label='Dist A')
ax.barh(r2, districtB_trees, color='green', height=bar_width, edgecolor='grey', label='Dist B')
ax.barh(r3, districtC_trees, color='red', height=bar_width, edgecolor='grey', label='Dist C')

ax.set_ylabel('Year', fontweight='bold', fontsize=12)
ax.set_xlabel('Trees Planted', fontweight='bold', fontsize=12)
ax.set_title('Annual Trees Planted by District (2015-20)', fontweight='bold', fontsize=14)
ax.set_yticks([r + bar_width for r in range(len(years))])
ax.set_yticklabels(years)

ax.legend()

ax.grid(True, linestyle='--', alpha=0.6, axis='x')
plt.tight_layout()

ax.annotate('Milestone', xy=(750, 4), xytext=(820, 2),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()