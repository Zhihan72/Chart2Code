import matplotlib.pyplot as plt
import numpy as np

# Data for monthly average temperatures in Aqualis (°C)
months = np.arange(1, 13)
avg_temperatures_2022 = np.array([5.5, 6.3, 10.8, 15.0, 19.5, 22.8, 17.5, 23.0, 20.5, 14.2, 7.2, 9.0])
avg_temperatures_2021 = np.array([4.8, 8.2, 9.1, 14.0, 18.4, 21.9, 16.8, 19.6, 22.1, 13.2, 6.5, 5.7])

# High and Low temperatures for each month in 2022
high_temperatures_2022 = np.array([8.0, 17.5, 10.0, 20.0, 28.5, 22.5, 15.0, 29.0, 26.0, 9.0, 12.0, 24.0])
low_temperatures_2022 = np.array([3.5, 4.5, 6.0, 17.0, 10.0, 15.0, 17.5, 12.0, 8.0, 11.0, 3.0, 6.5])

# Calculating the temperature range (difference between high and low temperatures)
temperature_range_2022 = high_temperatures_2022 - low_temperatures_2022

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Line chart for monthly average temperatures
ax1.plot(months, avg_temperatures_2022, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='2022')
ax1.plot(months, avg_temperatures_2021, marker='s', linestyle='--', color='#ff7f0e', linewidth=2, label='2021')

# Adding Titles and Labels
ax1.set_title('Monthly Average Temperatures in Aqualis (2021 vs 2022)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14)
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=12)

# Plot for temperature range (difference between high and low temperatures)
ax2.bar(months, temperature_range_2022, color='#2ca02c', label='Temperature Range', alpha=0.7)

# Adding Titles and Labels
ax2.set_title('Temperature Range in Aqualis (2022)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Month', fontsize=14)
ax2.set_ylabel('Temperature Range (°C)', fontsize=14)
ax2.set_xticks(months)
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()