import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.arange(2000, 2021)

# Data for the market share percentages for renewable energy sources (shuffled content)
solar = np.array([1.5, 1.2, 1, 2.8, 3.5, 5, 2, 6.5, 8, 10, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55])
wind = np.array([3, 2, 2, 4, 7, 5, 9, 12, 14, 22, 20, 18, 23, 24, 26, 27, 28, 30, 32, 33, 35])
hydro = np.array([12, 11, 10, 14, 13, 15, 16, 18, 17, 19, 20, 21, 21.5, 22, 23, 22.5, 23.5, 24, 24.5, 24, 25])
biomass = np.array([2, 1.5, 1, 3, 4, 3.5, 6, 5, 7, 8, 9, 9.5, 10.5, 10, 11, 11.5, 12.5, 12, 13, 12.5, 13.5])

energy_data = np.vstack([solar, wind, hydro, biomass])

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']
labels = ['Solar', 'Wind', 'Hydropower', 'Biomass']

ax.stackplot(years, energy_data, labels=labels, colors=colors, alpha=0.8)

ax.set_title('The Rise of Renewable Energy:\nMarket Share of Renewable Energy Sources (2000-2020)', fontsize=18, fontweight='bold', ha='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Market Share (%)', fontsize=14)

ax.legend(loc='upper left', fontsize=12, title='Renewable Sources')

significant_years = {
    'Solar': 2020,
    'Wind': 2015,
    'Hydropower': 2009,
    'Biomass': 2010
}
annotations = {
    'Solar': 55,
    'Wind': 18,
    'Hydropower': 21,
    'Biomass': 9
}

for source, year in significant_years.items():
    ax.annotate(f"{source}: {annotations[source]}%",
                xy=(year, annotations[source]), 
                xytext=(year - 10, annotations[source] + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
                fontsize=10, fontweight='bold', color='darkred')

ax.grid(linestyle='--', linewidth=0.7, alpha=0.5)

plt.tight_layout()
plt.show()