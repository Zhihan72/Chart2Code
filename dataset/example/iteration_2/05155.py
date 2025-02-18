import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Evolution of Renewable Energy Adoption
# This script visualizes the data on renewable energy adoption in different countries over several years. 
# It tracks Solar, Wind, and Hydropower capacities added each year from 2018 to 2022.

# Data: Capacity added in MW (Megawatts)
years = np.array([2018, 2019, 2020, 2021, 2022])
countries = ["USA", "China", "Germany", "India", "Brazil"]

# Data for each country (solar, wind, hydro)
usa_data = {"Solar": [10, 15, 20, 25, 30], "Wind": [5, 10, 15, 20, 25], "Hydro": [3, 4, 4, 5, 6]}
china_data = {"Solar": [20, 30, 40, 50, 60], "Wind": [15, 20, 25, 30, 35], "Hydro": [13, 14, 15, 16, 17]}
germany_data = {"Solar": [5, 10, 15, 20, 25], "Wind": [10, 15, 20, 25, 30], "Hydro": [2, 3, 3, 4, 4]}
india_data = {"Solar": [8, 12, 16, 20, 24], "Wind": [6, 9, 12, 15, 18], "Hydro": [4, 5, 5, 6, 7]}
brazil_data = {"Solar": [3, 6, 9, 12, 15], "Wind": [4, 5, 6, 7, 8], "Hydro": [5, 6, 7, 8, 9]}

all_data = [usa_data, china_data, germany_data, india_data, brazil_data]
energy_types = ["Solar", "Wind", "Hydro"]
colors = ['#FFD700', '#1E90FF', '#32CD32']

# Set up the figure and subplots
fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(12, 20), sharex=True)
fig.suptitle("Renewable Energy Adoption (2018-2022)", fontsize=18, fontweight='bold')

# Plot each country's data in separate subplots
for i, ax in enumerate(axes):
    country_data = all_data[i]
    for j, energy in enumerate(energy_types):
        ax.bar(years + j * 0.2, country_data[energy], width=0.2, color=colors[j], edgecolor='black', label=energy if i == 0 else "")
    ax.set_title(countries[i], fontsize=14, fontweight='bold')
    ax.set_ylabel('Capacity Added (MW)', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    ax.legend()

# Adjusting layout to prevent overlap
plt.xlabel("Year", fontsize=12, fontweight='bold')
plt.xticks(years)
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Show the plot
plt.show()