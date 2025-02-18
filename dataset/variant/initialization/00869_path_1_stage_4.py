import matplotlib.pyplot as plt
import numpy as np

# Data for the donut chart
energy_sources = ['Bio-Energy', 'Solar', 'Renewables', 'Hydro', 'Wind']
percentages = [20, 35, 5, 15, 25]
new_colors = ['#E63946', '#F1FAEE', '#A8DADC', '#457B9D', '#1D3557']

# Data for the bar chart
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
    startangle=90,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
axs[0].add_artist(centre_circle)
axs[0].set_title('EcoVision: Energy Mix 2025\nin FutureCity', fontsize=14, fontweight='bold')

plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=10)
axs[0].axis('equal')

axs[0].legend(wedges, energy_sources, title="Sources of Power", loc='center left', bbox_to_anchor=(1.3, 0.5), fontsize=10)
axs[0].annotate('Energy Shift\n2025', xy=(0, 0), fontsize=12, fontweight='bold', color='#444444', ha='center', va='center')

width = 0.15
bar_positions = np.arange(len(years))

axs[1].barh(bar_positions - 2*width, solar, width, label='Solar Energy', color='#F1FAEE')
axs[1].barh(bar_positions - width, wind, width, label='Wind Power', color='#1D3557')
axs[1].barh(bar_positions, biomass, width, label='Biomass Fuel', color='#E63946')
axs[1].barh(bar_positions + width, hydropower, width, label='Water Power', color='#457B9D')
axs[1].barh(bar_positions + 2*width, other_renewables, width, label='Alternative', color='#A8DADC')

axs[1].set_title('Annual Increase in Green Energy Capacity', fontsize=14, fontweight='bold')
axs[1].set_ylabel('Years', fontsize=12)
axs[1].set_xlabel('Percent Capacity', fontsize=12)
axs[1].set_yticks(bar_positions)
axs[1].set_yticklabels(years)
axs[1].legend(title="Types of Energies", fontsize=10, loc='lower right')

plt.tight_layout()
plt.show()