import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
countries = ["USA", "China", "Germany", "India", "Brazil"]

usa_data = {"Solar": [15, 10, 25, 20, 30], "Wind": [10, 5, 25, 15, 20], "Hydro": [4, 3, 5, 6, 4]}
china_data = {"Solar": [30, 20, 50, 40, 60], "Wind": [20, 15, 35, 25, 30], "Hydro": [14, 13, 16, 15, 17]}
germany_data = {"Solar": [10, 5, 20, 15, 25], "Wind": [15, 10, 30, 20, 25], "Hydro": [3, 2, 4, 3, 4]}
india_data = {"Solar": [12, 8, 20, 16, 24], "Wind": [9, 6, 15, 12, 18], "Hydro": [5, 4, 6, 5, 7]}
brazil_data = {"Solar": [6, 3, 12, 9, 15], "Wind": [5, 4, 7, 6, 8], "Hydro": [6, 5, 8, 7, 9]}

all_data = [usa_data, china_data, germany_data, india_data, brazil_data]
energy_types = ["Solar", "Wind", "Hydro"]
single_color = '#1E90FF'  # Using a single color for all bars

fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(12, 20), sharex=True)
fig.suptitle("Renewable Energy Adoption (2018-2022)", fontsize=18, fontweight='bold')

for i, ax in enumerate(axes):
    country_data = all_data[i]
    for j, energy in enumerate(energy_types):
        ax.bar(years + j * 0.2, country_data[energy], width=0.2, color=single_color, edgecolor='black', label=energy if i == 0 else "")
    ax.set_title(countries[i], fontsize=14, fontweight='bold')
    ax.set_ylabel('Capacity Added (MW)', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    if i == 0:  # Ensure the legend only appears on the first subplot
        ax.legend()

plt.xlabel("Year", fontsize=12, fontweight='bold')
plt.xticks(years)
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()