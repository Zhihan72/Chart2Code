import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Wind', 'Solar', 'Hydropower', 'Biomass', 'Geothermal', 'Other']
percentages = [27, 23, 18, 12, 8, 12]

colors = ['#2ca02c', '#9467bd', '#1f77b4', '#8c564b', '#ff7f0e', '#d62728']  # Shuffled colors

explode = (0, 0.1, 0, 0, 0, 0)  # Exploding a different sector than before

fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    percentages,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=90,  # Changed the starting angle
    colors=colors,
    explode=explode,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}  # Changed border color and width
)

ax.set_title(
    "Global Renewable Energy Mix in 2022",
    fontsize=16, fontweight='light', pad=15  # Adjusted title styling
)
plt.setp(autotexts, size=10, weight='normal', color='black')  # Changed text color and size
plt.setp(texts, size=10)

ax.axis('equal')

years = np.arange(2012, 2023)
growth = [8, 10, 12, 15, 18, 21, 24, 28, 32, 35, 40]

ax_inset = fig.add_axes([0.7, 0.2, 0.2, 0.25])  # Altered position of inset axes
ax_inset.plot(years, growth, linestyle='--', marker='o', color='green')  # Added line style and marker
ax_inset.set_title("Renewable Growth (2012-2022)", fontsize=9)
ax_inset.set_ylabel("Energy (%)", fontsize=7)
ax_inset.set_xlabel("Years", fontsize=7)
ax_inset.tick_params(axis='both', labelsize=7)

plt.legend(wedges, energy_sources, title="Energy Sources", loc="lower left", bbox_to_anchor=(0.7, 0.1, 0.5, 1), fontsize=8)  # Changed legend position and font size

plt.tight_layout()
plt.show()