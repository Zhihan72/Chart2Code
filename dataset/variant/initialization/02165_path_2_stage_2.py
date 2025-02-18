import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])
revenue_per_tourist = 1.0
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

# Sorting the revenue and years based on revenue in descending order
sorted_indices = np.argsort(space_revenue)[::-1]
sorted_years = years[sorted_indices]
sorted_space_revenue = space_revenue[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 9))

# Unified color
unified_color = '#FF5733'

ax1.bar(sorted_years, sorted_space_revenue, color=unified_color, alpha=0.6, label='Revenue ($M)', width=0.5)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Revenue (in millions)", fontsize=12, color=unified_color)
ax1.tick_params(axis='y', labelcolor=unified_color)

plt.title("Sorted Space Tourism Revenue\nfrom 2020 to 2030", fontsize=16, fontweight='bold', pad=20)

ax1.legend(loc='upper right')

# Set x-ticks as sorted years to maintain clarity in labeling
ax1.set_xticks(sorted_years)
ax1.set_yticks(np.arange(0, max(sorted_space_revenue) + 5, 5))

ax1.grid(True, linestyle='--', alpha=0.7)

fig.tight_layout()
plt.show()