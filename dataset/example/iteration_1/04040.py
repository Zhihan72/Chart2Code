import matplotlib.pyplot as plt
import numpy as np

# Context and Backstory
# We are analyzing the trend of renewable energy production over a decade (2010-2020) for three fictitious energy companies 
# (Solarance, WindGen, and HydroFlow) operating in a fictional city called EcoVille.

# Data for renewable energy production (in GWh) from 2010 to 2020
years = np.arange(2010, 2021)

solarance_production = [20, 25, 30, 40, 55, 60, 80, 85, 90, 95, 100]
windgen_production = [15, 20, 25, 30, 40, 50, 55, 60, 70, 80, 90]
hydroflow_production = [10, 12, 15, 18, 25, 35, 50, 55, 60, 65, 70]

# Plotting the data
plt.figure(figsize=(14, 8))

# Plot lines with markers for each company
plt.plot(years, solarance_production, marker='o', linestyle='-', color='#ffdd57', 
         label='Solarance (Solar Energy)', linewidth=2)
plt.plot(years, windgen_production, marker='^', linestyle='-', color='#1f77b4', 
         label='WindGen (Wind Energy)', linewidth=2)
plt.plot(years, hydroflow_production, marker='s', linestyle='-', color='#2ca02c', 
         label='HydroFlow (Hydropower)', linewidth=2)

# Add title and labels
plt.title('Renewable Energy Production Trends in EcoVille (2010-2020)', fontsize=18, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Production (GWh)', fontsize=14)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Set x-ticks and y-ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(10, 111, step=10))

# Add legend with title
plt.legend(loc='upper left', fontsize=12, title='Energy Companies', title_fontsize='14')

# Automatically adjust the layout
plt.tight_layout()

# Show plot
plt.show()