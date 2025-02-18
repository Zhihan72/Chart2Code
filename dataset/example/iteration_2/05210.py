import matplotlib.pyplot as plt
import numpy as np

# Backstory: Examining the Growth of Different Renewable Energy Sources Over a Decade
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

# Data: Installed capacity (in GW) for different renewable energy sources
solar_capacity = np.array([135, 186, 225, 305, 400, 480, 538, 625, 760, 850])
wind_capacity = np.array([320, 370, 400, 470, 530, 590, 650, 707, 745, 790])
hydro_capacity = np.array([1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1155, 1160])

# Configure subplot to include a bar chart and a line plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot bar chart for the year 2022
bar_width = 0.25
bar_positions = np.arange(len(years))

# Plot Solar Energy Capacity
bars_solar = ax1.bar(bar_positions - bar_width, solar_capacity, width=bar_width, color='gold', label='Solar', edgecolor='black')

# Plot Wind Energy Capacity
bars_wind = ax1.bar(bar_positions, wind_capacity, width=bar_width, color='skyblue', label='Wind', edgecolor='black')

# Plot Hydro Energy Capacity
bars_hydro = ax1.bar(bar_positions + bar_width, hydro_capacity, width=bar_width, color='steelblue', label='Hydro', edgecolor='black')

# Line plot showing the increment of each energy source capacity from the previous year (in %)
solar_increase = np.roll(np.diff(solar_capacity)/solar_capacity[:-1]*100, 1)
wind_increase = np.roll(np.diff(wind_capacity)/wind_capacity[:-1]*100, 1)
hydro_increase = np.roll(np.diff(hydro_capacity)/hydro_capacity[:-1]*100, 1)

# To prevent NaN appearance in the chart for increasing array
solar_increase[0] = 0
wind_increase[0] = 0
hydro_increase[0] = 0

ax2 = ax1.twinx()

# Plotting line for Solar
ax2.plot(bar_positions[1:], solar_increase, color='darkorange', marker='o', linestyle='--', linewidth=1.5, label='Solar Growth Rate (%)')

# Plotting line for Wind
ax2.plot(bar_positions[1:], wind_increase, color='deepskyblue', marker='s', linestyle='--', linewidth=1.5, label='Wind Growth Rate (%)')

# Plotting line for Hydro
ax2.plot(bar_positions[1:], hydro_increase, color='navy', marker='d', linestyle='--', linewidth=1.5, label='Hydro Growth Rate (%)')

# Annotations for bars
for bars in [bars_solar, bars_wind, bars_hydro]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.0f}GW', ha='center', va='bottom', fontsize=10)

# Chart titles and labels
ax1.set_title('Decade-long Growth of Renewable Energy Sources (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Years', fontsize=12)
ax1.set_ylabel('Installed Capacity (GW)', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

ax1.set_xticks(bar_positions)
ax1.set_xticklabels(years, rotation=45, ha='right', fontsize=11)

# Adding legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Grid for visual assistance
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Tight layout to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()