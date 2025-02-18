import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Bio-Energy', 'Solar', 'Renewables', 'Hydro', 'Wind']
percentages = [20, 35, 5, 15, 25]
new_colors = ['#1D3557', '#457B9D', '#A8DADC', '#F1FAEE', '#E63946']

years = np.arange(2020, 2026)
solar = [34, 36, 30, 35, 32, 38]
wind = [23, 27, 24, 25, 22, 26]
biomass = [19, 20, 18, 19, 20, 19]
hydropower = [15, 15, 12, 14, 15, 13]
other_renewables = [5, 5, 5, 5, 5, 5]

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

wedges, texts, autotexts = axs[0].pie(
    percentages,
    labels=energy_sources,
    colors=new_colors,
    autopct='%1.1f%%',
    startangle=120,
    pctdistance=0.75,
    wedgeprops=dict(width=0.4, edgecolor='gray'),
    explode=(0.03, 0.07, 0.05, 0.07, 0.03)
)

axs[0].add_artist(plt.Circle((0, 0), 0.60, fc='lightgray'))
axs[0].set_title('Energy Mix 2025 - FutureCity', fontsize=16, fontweight='normal')

plt.setp(autotexts, size=9, weight="light", color="darkred")
plt.setp(texts, size=9)
axs[0].axis('equal')

axs[0].legend(wedges, energy_sources, title="Sources", loc='lower left', bbox_to_anchor=(0.8, -0.1), fontsize=9)

width = 0.12
bar_positions = np.arange(len(years))

axs[1].bar(bar_positions, solar, width, label='Solar', color='g', hatch='/')
axs[1].bar(bar_positions + width, wind, width, label='Wind', color='b', hatch='\\')
axs[1].bar(bar_positions + 2*width, biomass, width, label='Biomass', color='r', hatch='|')
axs[1].bar(bar_positions + 3*width, hydropower, width, label='Hydro', color='c', hatch='-')
axs[1].bar(bar_positions + 4*width, other_renewables, width, label='Other', color='m', hatch='+')

axs[1].set_title('Yearly Green Energy Capacity Growth', fontsize=16, fontweight='normal')
axs[1].set_ylabel('Percentage (%)', fontsize=12)
axs[1].set_xlabel('Years', fontsize=12)
axs[1].set_xticks(bar_positions + 2*width)
axs[1].set_xticklabels(years)
axs[1].grid(True, axis='y', linestyle='--', linewidth=0.7)
axs[1].legend(title="Energy Types", fontsize=9, loc='upper left')

plt.tight_layout()
plt.show()