import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The local meteorological department has been tracking weather patterns over the past decade. 
# They aim to understand the fluctuations in average monthly temperatures over three distinct regions: Coastal, Inland, and Mountain.

# Data: Monthly average temperatures over 10 years for the three regions
years = np.arange(2013, 2023)
monthly_avg_temp_coastal = np.array([15, 16, 15.5, 16, 16.5, 17, 16.7, 17.2, 17.5, 18])
monthly_avg_temp_inland = np.array([10, 10.5, 10.3, 11, 10.8, 11.5, 11.3, 11.8, 12, 12.2])
monthly_avg_temp_mountain = np.array([5, 5.5, 5.3, 5.7, 6, 6.2, 6.4, 6.8, 7, 7.2])

# Spline interpolation for a smoother line representation
coastal_spline = make_interp_spline(years, monthly_avg_temp_coastal, k=3)  
inland_spline = make_interp_spline(years, monthly_avg_temp_inland, k=3)
mountain_spline = make_interp_spline(years, monthly_avg_temp_mountain, k=3)

years_smooth = np.linspace(years.min(), years.max(), 300)
coastal_temp_smooth = coastal_spline(years_smooth)
inland_temp_smooth = inland_spline(years_smooth)
mountain_temp_smooth = mountain_spline(years_smooth)

# Plot configuration
plt.figure(figsize=(14, 8))

# Line plot for each region
plt.plot(years_smooth, coastal_temp_smooth, label='Coastal Region', color='dodgerblue', linewidth=2)
plt.plot(years_smooth, inland_temp_smooth, label='Inland Region', color='forestgreen', linewidth=2)
plt.plot(years_smooth, mountain_temp_smooth, label='Mountain Region', color='darkred', linewidth=2)

# Scatter plots to show actual data points
plt.scatter(years, monthly_avg_temp_coastal, color='dodgerblue', edgecolors='black', s=50)
plt.scatter(years, monthly_avg_temp_inland, color='forestgreen', edgecolors='black', s=50)
plt.scatter(years, monthly_avg_temp_mountain, color='darkred', edgecolors='black', s=50)

# Title and labels
plt.title('Decadal Trends in Average Monthly Temperatures Across Regions', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=13)
plt.ylabel('Average Monthly Temperature (°C)', fontsize=13)

# Customizing x and y axis ticks
plt.xticks(np.arange(2013, 2024, step=1))
plt.yticks(np.arange(5, 19, step=1))
plt.legend(loc='upper left', fontsize=11, frameon=True)
plt.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to avoid text collision
plt.tight_layout()

# Display the plot
plt.show()