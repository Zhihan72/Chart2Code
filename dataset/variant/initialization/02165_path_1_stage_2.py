import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])
revenue_per_tourist = 1.0
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

sorted_indices = np.argsort(space_revenue)
sorted_years = years[sorted_indices]
sorted_space_tourists = space_tourists[sorted_indices]
sorted_space_revenue = space_revenue[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

# Randomly altering marker type and line styles
marker_types = ['o', 's', 'D', '<']
line_styles = ['-', '--', '-.', ':']
ax.plot(sorted_years, sorted_space_revenue, marker=np.random.choice(marker_types), linestyle=np.random.choice(line_styles), color='darkorange', label='Revenue ($M)')

ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Revenue (in millions)", fontsize=12, color='darkorange')
ax.tick_params(axis='y', labelcolor='darkorange')

milestones = {2021: "1K Tourists", 2023: "Space Hotel", 2026: "Flights Double", 2029: "30K Milestone"}
for year, label in milestones.items():
    idx = np.where(sorted_years == year)[0]
    if idx.size > 0:
        ax.annotate(label, (sorted_years[idx[0]], sorted_space_revenue[idx[0]]), textcoords="offset points", xytext=(10, -15), ha='right', fontsize=8, arrowprops=dict(arrowstyle='->', color='green'))

# Altering grid style
ax.grid(True, linestyle=np.random.choice(['--', '-.', ':']), alpha=0.5)

# Modifying the border color and style
for spine in ax.spines.values():
    spine.set_edgecolor(np.random.choice(['black', 'grey', 'darkblue', 'teal']))
    spine.set_linestyle(np.random.choice(['-', '--', '-.', ':']))

ax.set_xticks(sorted_years)
ax.set_yticks(np.arange(0, max(sorted_space_revenue) + 5, 5))

fig.tight_layout()
ax.legend(loc='upper left')
plt.title("Randomized Revenue from Space Tourism\n(2020 to 2030)", fontsize=14, fontweight='medium', pad=15)
plt.show()