import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Others']
consumption_percentages = [35, 25, 15, 10, 10, 5]

# Changed the order of colors
colors = ['#ffcc99', '#66b3ff', '#ffb3e6', '#c2c2f0', '#ff9999', '#99ff99']

# Modified explode to de-emphasize 'Solar'
explode = (0, 0, 0.1, 0, 0, 0)

# Changed the figsize and added a random line style for a border effect
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_frame_on(True)
ax.spines['top'].set_linestyle('dashed')
ax.spines['bottom'].set_linewidth(2)

wedges, texts, autotexts = ax.pie(
    consumption_percentages,
    explode=explode,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.80,
    textprops={'fontsize': 10},
    shadow=False
)

centre_circle = plt.Circle((0, 0), 0.65, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title('Energy Consumption Breakdown in 2023\nEco-Friendly Community', fontsize=14, fontweight='bold', pad=15)

# Adjusted legend location and added marker scale.
plt.legend(wedges, energy_sources, title="Energy Sources", loc="upper right", bbox_to_anchor=(1, 1), markerfirst=False)

# Added grid lines
ax.yaxis.grid(True, linestyle='--')

plt.tight_layout()

plt.show()