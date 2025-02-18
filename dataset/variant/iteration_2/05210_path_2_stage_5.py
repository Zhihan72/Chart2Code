import matplotlib.pyplot as plt
import numpy as np

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

solar_capacity = np.array([135, 186, 225, 305, 400, 480, 538, 625, 760, 850])
wind_capacity = np.array([320, 370, 400, 470, 530, 590, 650, 707, 745, 790])
hydro_capacity = np.array([1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1155, 1160])
geothermal_capacity = np.array([30, 35, 40, 50, 60, 70, 80, 88, 95, 105])  # Adding new data series

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_height = 0.2
bar_positions = np.arange(len(years))

ax1.barh(bar_positions - 1.5*bar_height, solar_capacity, height=bar_height, 
         color='blue', edgecolor='white', label='Solar Capacity', linestyle='solid')
ax1.barh(bar_positions - 0.5*bar_height, wind_capacity, height=bar_height, 
         color='red', edgecolor='white', label='Wind Capacity', linestyle='dashed')
ax1.barh(bar_positions + 0.5*bar_height, hydro_capacity, height=bar_height, 
         color='cyan', edgecolor='white', label='Hydro Capacity', linestyle='dotted')
ax1.barh(bar_positions + 1.5*bar_height, geothermal_capacity, height=bar_height, 
         color='green', edgecolor='white', label='Geothermal Capacity', linestyle='dashdot')  # New bar

ax1.set_yticks(bar_positions)
ax1.set_yticklabels(years)
ax1.set_xlabel('Capacity (MW)')
ax1.set_ylabel('Year')
ax1.yaxis.grid(False)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.legend(loc='upper left', fontsize=12)

plt.tight_layout()

plt.show()