import matplotlib.pyplot as plt
import numpy as np

# Title and backstory:
# This script visualizes the hypothetical energy production trends from different sources
# over a span of 50 years, from 1970 to 2020. It also highlights the decline of fossil fuels
# and the rise of renewable energy sources during the period. The data is explicitly constructed
# to reflect the general global shift in energy production practices.

# Define years from 1970 to 2020
years = np.arange(1970, 2021)

# Energy production data (in terawatt-hours) from various sources (Fossil Fuels, Solar, Wind, Hydro, Nuclear)
fossil_fuels = [12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500,
                17000, 17000, 16800, 16600, 16400, 16000, 15800, 15600, 15500, 15400,
                15300, 15000, 14500, 14000, 13500, 13000, 12600, 12200, 11800, 11400,
                10800, 10300, 10000, 9800, 9600, 9400, 9200, 9000, 8800, 8600,
                8350, 8100, 7900, 7650, 7400, 7150, 6900, 6650, 6400, 6200, 6000]

solar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
         20, 30, 50, 70, 100, 150, 200, 270, 350, 450,
         600, 800, 1050, 1300, 1600, 2000, 2500, 3100, 3800, 4500,
         5200, 5900, 6500, 7400, 8200, 9000, 9800, 10500, 11200, 11900,
         12600, 13300, 14100, 14800, 15600, 16400, 17200, 18100, 19000, 20000, 21000]

wind = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20,
        50, 80, 110, 160, 210, 260, 320, 400, 480, 580,
        700, 850, 1000, 1200, 1400, 1650, 1900, 2200, 2550, 2900,
        3300, 3700, 4150, 4700, 5300, 5900, 6500, 7150, 7850, 8600,
        9300, 10100, 11000, 11800, 12600, 13400, 14300, 15100, 16000, 17000, 18000]

hydro = [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3750, 3800,
         3850, 3900, 4000, 4100, 4200, 4300, 4500, 4700, 4800, 4900,
         5000, 5100, 5200, 5400, 5600, 5700, 5800, 5900, 6000, 6100,
         6200, 6300, 6400, 6500, 6600, 6750, 6900, 7050, 7200, 7400,
         7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600]

nuclear = [0, 0, 0, 50, 100, 200, 300, 400, 500, 600,
           700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600,
           1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600,
           2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600,
           3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700]

# Convert lists to numpy arrays for easier arithmetic operations
fossil_fuels = np.array(fossil_fuels)
solar = np.array(solar)
wind = np.array(wind)
hydro = np.array(hydro)
nuclear = np.array(nuclear)

# Combine the data for stackplot
energy_data = np.row_stack([fossil_fuels, solar, wind, hydro, nuclear])

# Define labels and colors for the energy sources
sources = ['Fossil Fuels', 'Solar', 'Wind', 'Hydro', 'Nuclear']
colors = ['#FFA07A', '#FFD700', '#87CEFA', '#7FFFD4', '#D8BFD8']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create the stacked area plot
ax.stackplot(years, energy_data, labels=sources, colors=colors, alpha=0.85)

# Overlay a line plot highlighting the total energy production
total_energy = energy_data.sum(axis=0)
ax.plot(years, total_energy, color='black', linewidth=2.5, marker='o', label='Total Energy Production')

# Titles and labels
ax.set_title("Global Energy Production Trends (1970-2020)\nShift from Fossil Fuels to Renewable Sources", 
             fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Customize the grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add a legend outside the plot to avoid clutter
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Energy Sources')

# Add annotations to highlight significant milestones
ax.annotate('Start of Solar Expansion', xy=(1980, 100), xytext=(1985, 15000),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Wind Energy Surge', xy=(2000, 700), xytext=(2005, 20000),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Hydro Stabilization', xy=(1995, 4500), xytext=(2000, 15000),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()