import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Existing data for PM2.5 concentration and asthma cases
pm25_concentration = np.array([35, 38, 37, 36, 39, 41, 43, 42, 40, 38, 35])
asthma_cases = np.array([120, 130, 125, 135, 140, 150, 160, 155, 145, 135, 125])

# New synthetic data for another health impact: respiratory illness visits (in thousands)
respiratory_visits = np.array([80, 85, 82, 88, 90, 95, 100, 98, 92, 89, 86])

# Errors for PM2.5 concentration variability
errors_pm25 = np.array([2 for _ in range(len(years))])

# Plotting the chart with a twin Y-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot PM2.5 concentration
ax1.errorbar(years, pm25_concentration, yerr=errors_pm25, label='PM2.5 Concentration (µg/m³)', fmt='-o', capsize=5, color='tab:blue', alpha=0.8)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=14, color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Second y-axis for asthma cases
ax2 = ax1.twinx()
ax2.plot(years, asthma_cases, label='Asthma Cases (thousands)', linestyle='--', marker='s', color='tab:red', alpha=0.8)
ax2.set_ylabel('Asthma Cases (thousands)', fontsize=14, color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Adding a third series for respiratory illness visits on a secondary axis
ax2.plot(years, respiratory_visits, label='Respiratory Visits (thousands)', linestyle='-.', marker='^', color='tab:green', alpha=0.8)

# Title
plt.title("Trends in Air Pollution and Health Impacts in Megacity (2010-2020)", fontsize=16, fontweight='bold', wrap=True)

# Adding gridlines for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Adding legends
ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 1.1), fontsize=12)
ax2.legend(loc='upper right', bbox_to_anchor=(0.99, 1.1), fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()