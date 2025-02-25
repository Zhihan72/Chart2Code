import matplotlib.pyplot as plt
import numpy as np

# Altering energy source labels and their order
energy_sources = ['GeoThermal', 'Hydro Power', 'Bio Mass', 'Solar', 'Wind Power', 'Alternative']
consumption_percentages = [10, 15, 10, 35, 25, 5]

colors = ['#ffcc99', '#66b3ff', '#ffb3e6', '#c2c2f0', '#ff9999', '#99ff99']
explode = (0, 0.1, 0, 0, 0, 0)

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

# Randomly altered chart title
plt.title('Eco Stats: 2023 Energy Usage\nCommunity Insights', fontsize=14, fontweight='bold', pad=15)

plt.legend(wedges, energy_sources, title="Alt Energy Sources", loc="upper right", bbox_to_anchor=(1, 1), markerfirst=False)

ax.yaxis.grid(True, linestyle='--')

plt.tight_layout()

plt.show()