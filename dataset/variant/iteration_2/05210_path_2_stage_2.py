import matplotlib.pyplot as plt
import numpy as np

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

solar_capacity = np.array([135, 186, 225, 305, 400, 480, 538, 625, 760, 850])
wind_capacity = np.array([320, 370, 400, 470, 530, 590, 650, 707, 745, 790])
hydro_capacity = np.array([1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1155, 1160])

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_height = 0.25
bar_positions = np.arange(len(years))

ax1.barh(bar_positions - bar_height, solar_capacity, height=bar_height, color='gold', edgecolor='black', label='Solar Capacity')
ax1.barh(bar_positions, wind_capacity, height=bar_height, color='skyblue', edgecolor='black', label='Wind Capacity')
ax1.barh(bar_positions + bar_height, hydro_capacity, height=bar_height, color='steelblue', edgecolor='black', label='Hydro Capacity')

ax1.set_yticks(bar_positions)
ax1.set_yticklabels(years)
ax1.set_xlabel('Capacity (MW)')
ax1.set_ylabel('Year')
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

plt.tight_layout()

plt.show()