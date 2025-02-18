import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
districtA_trees = np.array([500, 550, 620, 700, 750, 800])
districtB_trees = np.array([600, 620, 640, 680, 720, 760])

bar_width = 0.25
r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(r1, districtA_trees, color='navy', height=bar_width, edgecolor='white', linestyle='-', label='District A')
ax.barh(r2, districtB_trees, color='crimson', height=bar_width, edgecolor='black', linestyle='-.', label='District B')

ax.set_ylabel('Year', fontweight='normal', fontsize=10)
ax.set_xlabel('Number of Trees', fontweight='light', fontsize=11)
ax.set_title('Trees Planted Per District (2015 - 2020)', fontweight='bold', fontsize=16)

ax.set_yticks([r + bar_width / 2 for r in range(len(years))])
ax.set_yticklabels(years)

ax.legend(loc='upper right', fontsize=10, title='Legend', title_fontsize=11)

ax.grid(True, linestyle=':', alpha=0.5, axis='both')

ax.annotate('Milestone', xy=(750, 4), xytext=(850, 2.5),
            arrowprops=dict(edgecolor='red', arrowstyle='-|>'), fontsize=11, color='purple')

plt.tight_layout()
plt.show()