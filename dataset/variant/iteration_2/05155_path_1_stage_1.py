import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])

# Data for each country (solar, wind, hydro)
usa_data = {"Solar": [10, 15, 20, 25, 30], "Wind": [5, 10, 15, 20, 25], "Hydro": [3, 4, 4, 5, 6]}
china_data = {"Solar": [20, 30, 40, 50, 60], "Wind": [15, 20, 25, 30, 35], "Hydro": [13, 14, 15, 16, 17]}
germany_data = {"Solar": [5, 10, 15, 20, 25], "Wind": [10, 15, 20, 25, 30], "Hydro": [2, 3, 3, 4, 4]}
india_data = {"Solar": [8, 12, 16, 20, 24], "Wind": [6, 9, 12, 15, 18], "Hydro": [4, 5, 5, 6, 7]}
brazil_data = {"Solar": [3, 6, 9, 12, 15], "Wind": [4, 5, 6, 7, 8], "Hydro": [5, 6, 7, 8, 9]}

all_data = [usa_data, china_data, germany_data, india_data, brazil_data]
energy_types = ["Solar", "Wind", "Hydro"]
colors = ['#FFD700', '#1E90FF', '#32CD32']

fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(12, 20), sharex=True)

for i, ax in enumerate(axes):
    country_data = all_data[i]
    for j, energy in enumerate(energy_types):
        ax.bar(years + j * 0.2, country_data[energy], width=0.2, color=colors[j], edgecolor='black')
    ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.xticks(years)
plt.tight_layout()

plt.show()