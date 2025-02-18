import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the fictional town of Greenfield, interest in renewable energy sources has surged over the last decade. This plot 
# shows the annual growth in solar panel installations, electric car purchases, and domestic wind turbine installations 
# from 2010 to 2020. The goal is to visualize how the town's commitment to green energy has evolved.

# Time period from 2010 to 2020
years = np.arange(2010, 2021)

# Number of solar panel installations each year
solar_panels = [50, 55, 60, 70, 85, 100, 120, 140, 160, 180, 210]

# Number of electric car purchases each year
electric_cars = [20, 25, 30, 45, 60, 90, 130, 175, 220, 280, 350]

# Number of domestic wind turbine installations each year
wind_turbines = [5, 7, 10, 15, 20, 30, 45, 65, 85, 110, 150]

fig, ax = plt.subplots(figsize=(14, 8))

# Plot the line chart with different styles for distinctiveness
ax.plot(years, solar_panels, marker='o', linestyle='-', color='orange', linewidth=2.5, markersize=8, label='Solar Panels')
ax.plot(years, electric_cars, marker='^', linestyle='--', color='blue', linewidth=2.5, markersize=8, label='Electric Cars')
ax.plot(years, wind_turbines, marker='s', linestyle='-.', color='green', linewidth=2.5, markersize=8, label='Wind Turbines')

# Enhance the grid for readability
ax.grid(True, linestyle='--', alpha=0.6)

# Title and labels with detailed description
ax.set_title('Greenfield’s Renewable Energy Adoption Over Time\n(2010-2020)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Installations', fontsize=14)

# Legend to describe the various data
ax.legend(loc='upper left', fontsize=12)

# Annotation for significant milestones
ax.annotate('Govt. Incentives Introduced', xy=(2014, 85), xytext=(2012, 140),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, ha='center', fontweight='bold')

ax.annotate('Community Campaign for Renewables', xy=(2017, 140), xytext=(2019, 100),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, ha='center', fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()