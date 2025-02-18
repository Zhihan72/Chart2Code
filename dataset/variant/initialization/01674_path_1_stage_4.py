import matplotlib.pyplot as plt
import numpy as np

mission_types = ['Human Spaceflight', 'Lunar Research', 'Technological Demonstration', 
                 'Deep Space Probes', 'Astronomical Observation', 'Planetary Exploration']
mission_counts = [10, 15, 20, 25, 30, 40]
mission_budgets = [100, 180, 150, 220, 250, 300]

colors = ['#ff9999', '#c2c2f0', '#ffcc99', '#ffb3e6', '#66b3ff', '#99ff99']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7),
                               gridspec_kw={'width_ratios': [1, 1.2]})

wedges, texts, autotexts = ax1.pie(
    mission_counts,
    labels=mission_types,
    autopct='%1.1f%%',
    startangle=125,
    colors=colors,
    pctdistance=0.9,
    wedgeprops=dict(width=0.35, edgecolor='gray', linestyle=':'),
    textprops={'fontsize': 11, 'color': 'darkblue'}
)

ax1.text(0, 0, 'AstroVentures\nMissions\n2013-2023',
         horizontalalignment='center', verticalalignment='center',
         fontsize=13, fontweight='bold', color='teal')

ax1.set_title("Space Mission Distribution\n(2013-2023)",
              fontsize=15, fontweight='bold', color='teal', pad=20)

ax2.barh(mission_types, mission_budgets, color=colors, edgecolor='gray', linestyle='-.')
ax2.set_xlabel('Budget in Millions ($)', fontsize=13)
ax2.set_title("Estimated Budget Allocation\nby Mission Type",
              fontsize=15, fontweight='bold', color='teal', pad=20)

ax2.grid(True, linestyle='--', linewidth=0.5, color='gray', axis='x')

for i, (count, budget) in enumerate(zip(mission_counts, mission_budgets)):
    ax2.text(budget + 5, i, f'${budget}M', va='center', fontsize=11, color='darkblue')

plt.tight_layout()
plt.show()