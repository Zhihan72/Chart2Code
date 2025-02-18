import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monitoring the health impacts of air pollution in Megacity over a decade
# The chart will illustrate the trends in particulate matter (PM2.5) concentration and the number of asthma cases in Megacity from 2010 to 2020.

# Define the years
years = np.arange(2010, 2021)

# Synthetic data for PM2.5 concentration (in µg/m³) in Megacity over the years
pm25_concentration = np.array([35, 38, 37, 36, 39, 41, 43, 42, 40, 38, 35])

# Synthetic data for the number of annual asthma cases (in thousands) in Megacity over the years
asthma_cases = np.array([120, 130, 125, 135, 140, 150, 160, 155, 145, 135, 125])

# Errors representing variability in the yearly reported PM2.5 concentration
errors_pm25 = np.array([2 for _ in range(len(years))])

# Plotting the chart with a twin Y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot PM2.5 concentration
ax1.errorbar(years, pm25_concentration, yerr=errors_pm25, label='PM2.5 Concentration (µg/m³)', fmt='-o', capsize=5, color='tab:blue', alpha=0.8)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=14, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Creating a second y-axis
ax2 = ax1.twinx()
ax2.plot(years, asthma_cases, label='Asthma Cases (thousands)', linestyle='--', marker='s', color='tab:red', alpha=0.8)
ax2.set_ylabel('Asthma Cases (thousands)', fontsize=14, color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Title
plt.title("Trends in Air Pollution and Asthma Cases in Megacity (2010-2020)", fontsize=16, fontweight='bold', wrap=True)

# Adding gridlines for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Adding legends
ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 0.95), fontsize=12)
ax2.legend(loc='upper right', bbox_to_anchor=(0.99, 0.95), fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()