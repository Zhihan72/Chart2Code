import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The data below portrays the monthly average temperatures in a fictional coastal city called "Aqualis" over a year. 
# The city has recently been subjected to significant seasonal variations resulting in notable temperature changes.
# We'll visualize these changes using a line chart and a supplementary plot to show the difference between the highest and lowest temperatures recorded each month.

# Data for monthly average temperatures in Aqualis (°C)
months = np.arange(1, 13)
avg_temperatures_2022 = np.array([5.5, 7.2, 10.8, 15.0, 17.5, 20.5, 23.0, 22.8, 19.5, 14.2, 9.0, 6.3])
avg_temperatures_2021 = np.array([4.8, 6.5, 9.1, 14.0, 16.8, 19.6, 22.1, 21.9, 18.4, 13.2, 8.2, 5.7])

# High and Low temperatures for each month in 2022
high_temperatures_2022 = np.array([8.0, 10.0, 15.0, 20.0, 22.5, 26.0, 29.0, 28.5, 24.0, 17.5, 12.0, 9.0])
low_temperatures_2022 = np.array([3.0, 4.5, 6.5, 10.0, 12.0, 15.0, 17.5, 17.0, 15.0, 11.0, 6.0, 3.5])

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

# Setting the x-axis tick marks to represent months
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Adding grid for better readability
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Adding a legend
ax1.legend(loc='upper left', fontsize=12)

# Plot for temperature range (difference between high and low temperatures)
ax2.bar(months, temperature_range_2022, color='#2ca02c', label='Temperature Range', alpha=0.7)

# Adding Titles and Labels
ax2.set_title('Temperature Range in Aqualis (2022)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Month', fontsize=14)
ax2.set_ylabel('Temperature Range (°C)', fontsize=14)

# Setting the x-axis tick marks to represent months
ax2.set_xticks(months)
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Adding grid for better readability
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adding a legend
ax2.legend(loc='upper right', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()