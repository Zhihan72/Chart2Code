import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Wind', 'Solar', 'Hydropower', 'Biomass', 'Other', 'Geothermal']
percentages = [27, 23, 18, 12, 12, 8]

single_color = '#2ca02c'

explode = (0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=90,
    colors=[single_color] * len(energy_sources),
    explode=explode,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
)

ax.set_title(
    "2022 Energy Mix Global Overview",
    fontsize=16, fontweight='light', pad=15
)
plt.setp(autotexts, size=10, weight='normal', color='black')
plt.setp(texts, size=10)

ax.axis('equal')

years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]

ax_inset = fig.add_axes([0.7, 0.2, 0.2, 0.25])
ax_inset.plot(years, growth, linestyle='--', marker='o', color='green')
ax_inset.set_title("Growth of Renewables (2012-2022)", fontsize=9)
ax_inset.set_ylabel("Percentage (%)", fontsize=7)
ax_inset.set_xlabel("Yearly Progress", fontsize=7)
ax_inset.tick_params(axis='both', labelsize=7)

plt.legend(wedges, energy_sources, title="Types of Energy", loc="lower left", bbox_to_anchor=(0.7, 0.1, 0.5, 1), fontsize=8)

plt.tight_layout()
plt.show()