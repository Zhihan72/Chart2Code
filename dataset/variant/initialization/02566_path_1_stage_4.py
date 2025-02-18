import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
parks = np.array([10, 15, 25, 35, 45, 55, 65, 75, 90, 100, 120])
gardens = np.array([5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60])
reserves = np.array([2, 4, 6, 10, 15, 20, 25, 30, 35, 40, 50])
community_spaces = np.array([1, 3, 5, 7, 10, 12, 15, 18, 22, 25, 30])

parks_cumulative = np.cumsum(parks)
gardens_cumulative = np.cumsum(gardens)
reserves_cumulative = np.cumsum(reserves)
community_spaces_cumulative = np.cumsum(community_spaces)

fig, ax = plt.subplots(figsize=(12, 8))

single_color = '#66c2a5'
ax.stackplot(years, parks_cumulative, gardens_cumulative, reserves_cumulative, community_spaces_cumulative,
             colors=[single_color] * 4, alpha=0.7)

ax.set_title('EcoVille Expansion: Greener Cities Over Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline of Expansion', fontsize=12)
ax.set_ylabel('Total Green Area Accumulation (Ha)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()