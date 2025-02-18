import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Biomass', 'Hydro']
percentages = [35, 25, 20, 15]

colors = ['#9400D3', '#FF6347', '#20B2AA', '#FFA07A']

years = np.arange(2020, 2026)
solar = [30, 32, 34, 35, 36, 38]
wind = [22, 23, 24, 25, 26, 27]
biomass = [18, 19, 19, 20, 20, 20]
hydropower = [12, 13, 14, 15, 15, 15]

fig, axs = plt.subplots(2, 1, figsize=(8, 12))

wedges, texts, autotexts = axs[0].pie(
    percentages, 
    labels=energy_sources, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=45, 
    pctdistance=0.9,
    wedgeprops=dict(width=0.4, edgecolor='#444444'),
    explode=(0.1, 0.05, 0.05, 0),
    shadow=False
)

centre_circle = plt.Circle((0, 0), 0.50, fc='#f0f0f0')
axs[0].add_artist(centre_circle)
axs[0].set_title('GreenTech Insights', fontsize=16, fontweight='light')

plt.setp(autotexts, size=8, weight="light", color="black")
plt.setp(texts, size=9)
axs[0].axis('equal')

axs[0].legend(wedges, energy_sources, title="Energy Sources", loc='upper right', bbox_to_anchor=(1.2, 1.0), fontsize=9)
axs[0].annotate('Renewable Sources', xy=(0, 0), fontsize=10, fontweight='regular', color='#333333', ha='center', va='center')

width = 0.2
bar_positions = np.arange(len(years))

axs[1].bar(bar_positions - 1.5*width, solar, width, label='Solar', hatch='//', color='#9400D3')
axs[1].bar(bar_positions - 0.5*width, wind, width, label='Wind', hatch='\\', color='#FF6347')
axs[1].bar(bar_positions + 0.5*width, biomass, width, label='Biomass', hatch='-', color='#20B2AA')
axs[1].bar(bar_positions + 1.5*width, hydropower, width, label='Hydro', hatch='.', color='#FFA07A')

axs[1].set_title('Renewable Growth Over Years', fontsize=16, fontweight='light')
axs[1].set_xlabel('Year', fontsize=10)
axs[1].set_ylabel('Capacity Share (%)', fontsize=10)
axs[1].set_xticks(bar_positions)
axs[1].set_xticklabels(years)
axs[1].legend(title="Energy Sources", fontsize=9, loc='upper center')
axs[1].grid(True, which='major', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()