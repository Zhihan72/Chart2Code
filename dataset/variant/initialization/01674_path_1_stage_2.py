import matplotlib.pyplot as plt
import numpy as np

mission_types = ['Planetary Exploration', 'Astronomical Observation', 
                 'Technological Demonstration', 'Human Spaceflight']
mission_counts = [40, 30, 20, 10]
mission_budgets = [300, 250, 150, 100]

colors = ['#66b3ff', '#ffcc99', '#99ff99', '#ff9999']

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