import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Nuclear', 'Biomass']
energy_percentages = [40, 30, 12, 8, 6, 4]

colors = ['#FFD700', '#1E90FF', '#00CED1', '#FF4500', '#9400D3', '#8B4513']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect='equal'))

explode = (0.1, 0, 0, 0, 0, 0)
wedges, _, autotexts = ax.pie(
    energy_percentages,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='black', linewidth=1.5),
    shadow=True
)

plt.setp(autotexts, size=10, weight='bold', color='black')

ax.legend(
    wedges, energy_sources,
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

plt.tight_layout()
plt.show()