import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking Renewable Energy Adoption Trends and Environmental Benefits (2020-2030)

# Data years
years = np.arange(2020, 2031)

# Renewable energy adoption data (in gigawatts)
solar_power = np.array([125, 140, 160, 180, 205, 230, 260, 290, 320, 355, 390])
wind_power = np.array([150, 170, 195, 220, 250, 280, 315, 350, 385, 420, 460])
hydropower = np.array([200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370])
geothermal = np.array([30, 33, 35, 38, 42, 45, 50, 55, 60, 65, 70])
biomass = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

# Environmental benefits data
CO2_reduction = np.array([100, 120, 140, 160, 185, 210, 240, 270, 300, 340, 380])
deforestation_prevented = np.array([50, 55, 63, 70, 80, 90, 100, 115, 130, 150, 170])

# Calculate cumulative data for stacked area plot
cumulative_wind = solar_power + wind_power
cumulative_hydropower = cumulative_wind + hydropower
cumulative_geothermal = cumulative_hydropower + geothermal
cumulative_biomass = cumulative_geothermal + biomass

# Initialize the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Stacked Area plot for Renewable Energy Adoption
ax1.fill_between(years, 0, solar_power, color='#FFD700', alpha=0.7, label='Solar Power')
ax1.fill_between(years, solar_power, cumulative_wind, color='#00BFFF', alpha=0.7, label='Wind Power')
ax1.fill_between(years, cumulative_wind, cumulative_hydropower, color='#008000', alpha=0.7, label='Hydropower')
ax1.fill_between(years, cumulative_hydropower, cumulative_geothermal, color='#FF6347', alpha=0.7, label='Geothermal')
ax1.fill_between(years, cumulative_geothermal, cumulative_biomass, color='#8B4513', alpha=0.7, label='Biomass')

ax1.set_title('Renewable Energy Adoption Trends (2020-2030)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (in GW)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, title='Energy Sources', title_fontsize='12')
ax1.grid(True, alpha=0.5, linestyle='--')

# Line plot for Environmental Benefits
ln1 = ax2.plot(years, CO2_reduction, color='blue', linewidth=2.5, marker='o', label='CO2 Reduction (in MMT)')
ln2 = ax2.plot(years, deforestation_prevented, color='green', linewidth=2.5, marker='s', label='Deforestation Prevented (in 1000 hectares)')

ax2.set_title('Environmental Benefits from Renewable Energy (2020-2030)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Environment Benefits', fontsize=12)
ax2.legend(loc='upper left', fontsize=10, title='Impact Metrics', title_fontsize='12')
ax2.grid(True, alpha=0.5, linestyle='--')

# Annotate significant points in the line plots
ax2.annotate('Major Solar Expansion', xy=(2025, 210), xytext=(2022, 250), 
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5), 
             fontsize=10, color='black', fontweight='bold')

ax2.annotate('Peak Deforestation Prevention', xy=(2030, 170), xytext=(2026, 130), 
             arrowprops=dict(facecolor='darkgreen', arrowstyle='->', linewidth=1.5), 
             fontsize=10, color='darkgreen', fontweight='bold')

# Adjust layout to prevent overlap and allow better readability
plt.tight_layout()

# Show plot
plt.show()