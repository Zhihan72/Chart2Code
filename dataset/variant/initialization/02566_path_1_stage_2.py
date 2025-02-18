import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
parks = np.array([10, 15, 25, 35, 45, 55, 65, 75, 90, 100, 120])
gardens = np.array([5, 7, 10, 15, 20, 25, 30, 35, 40, 50, 60])
reserves = np.array([2, 4, 6, 10, 15, 20, 25, 30, 35, 40, 50])

parks_cumulative = np.cumsum(parks)
gardens_cumulative = np.cumsum(gardens)
reserves_cumulative = np.cumsum(reserves)

fig, ax = plt.subplots(figsize=(12, 8))

# Apply a single color consistently across all data groups
single_color = '#66c2a5'
ax.stackplot(years, parks_cumulative, gardens_cumulative, reserves_cumulative,
             colors=[single_color, single_color, single_color], alpha=0.7)

ax.set_title('Urban Green Space Expansion: A Decade of Greener Living\nEcoVille, 2020-2030', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Cumulative Green Space Area (Hectares)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()