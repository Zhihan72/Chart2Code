import matplotlib.pyplot as plt
import numpy as np

sectors = ['Tidal Power', 'Geothermal Energy', 'Bioenergy']
power_sources = ['Tidal Generators', 'Hydrothermal Vents', 'Hydrogen Cells', 'Biomass']

energy_data = [
    [50, 10, 20, 20],
    [10, 60, 20, 10],
    [20, 10, 20, 50]
]

efficiency_ratios = [0.8, 0.6, 0.7]

colors = ['#81C784', '#FF8A65', '#FFD54F']

fig, ax = plt.subplots(2, 2, figsize=(16,16))
plt.subplots_adjust(top=0.85)

explode = (0.1, 0, 0, 0)

for i in range(len(sectors)):
    ax.flatten()[i].pie(
        energy_data[i],
        colors=colors,
        explode=explode
    )

ax_eff = fig.add_subplot(224)
ax_eff.bar(sectors, efficiency_ratios, color=colors)

plt.tight_layout(rect=[0, 0, 0.85, 0.95])
plt.show()