import matplotlib.pyplot as plt
import numpy as np

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

solar_capacity = np.array([135, 186, 225, 305, 400, 480, 538, 625, 760, 850])
wind_capacity = np.array([320, 370, 400, 470, 530, 590, 650, 707, 745, 790])
hydro_capacity = np.array([1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1155, 1160])

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 0.25
bar_positions = np.arange(len(years))

ax1.bar(bar_positions - bar_width, solar_capacity, width=bar_width, color='gold', edgecolor='black')
ax1.bar(bar_positions, wind_capacity, width=bar_width, color='skyblue', edgecolor='black')
ax1.bar(bar_positions + bar_width, hydro_capacity, width=bar_width, color='steelblue', edgecolor='black')

solar_increase = np.roll(np.diff(solar_capacity)/solar_capacity[:-1]*100, 1)
wind_increase = np.roll(np.diff(wind_capacity)/wind_capacity[:-1]*100, 1)
hydro_increase = np.roll(np.diff(hydro_capacity)/hydro_capacity[:-1]*100, 1)

solar_increase[0] = 0
wind_increase[0] = 0
hydro_increase[0] = 0

ax2 = ax1.twinx()

ax2.plot(bar_positions[1:], solar_increase, color='darkorange', marker='o', linestyle='--', linewidth=1.5)
ax2.plot(bar_positions[1:], wind_increase, color='deepskyblue', marker='s', linestyle='--', linewidth=1.5)
ax2.plot(bar_positions[1:], hydro_increase, color='navy', marker='d', linestyle='--', linewidth=1.5)

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()