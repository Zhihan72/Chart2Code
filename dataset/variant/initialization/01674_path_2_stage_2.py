import matplotlib.pyplot as plt
import numpy as np

# Shuffle the contents of mission_counts and mission_budgets manually
mission_types = ['Planetary', 'Observation', 'Tech Demo', 'Human Flight']
mission_counts = [10, 20, 30, 40]  # Altered the order of counts randomly
mission_budgets = [100, 150, 250, 300]  # Altered the order of budgets randomly
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1.2]})

wedges, texts, autotexts = ax1.pie(
    mission_counts,
    labels=mission_types,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops={'fontsize': 10, 'color': 'black'}
)

ax1.text(0, 0, 'Astro Missions\n2013-2023',
         horizontalalignment='center', verticalalignment='center',
         fontsize=12, fontweight='bold', color='navy')

ax1.set_title("Mission Types\n(2013-2023)",
              fontsize=14, fontweight='bold', color='navy', pad=20)

ax2.barh(mission_types, mission_budgets, color=colors, edgecolor='black')
ax2.set_xlabel('Budget ($M)', fontsize=12)
ax2.set_title("Budget by Type",
              fontsize=14, fontweight='bold', color='navy', pad=20)

for i, (count, budget) in enumerate(zip(mission_counts, mission_budgets)):
    ax2.text(budget + 5, i, f'${budget}M', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()