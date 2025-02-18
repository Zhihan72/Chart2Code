import matplotlib.pyplot as plt
import numpy as np

# Pie chart data: Renewable energy sources and their usage percentages
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass']
usage_percentages = [30, 25, 20, 15, 10]

# Subplot data: Annual growth data for each energy source (in percentage)
years = np.arange(2010, 2024)
solar_growth = [5, 7, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 26]
wind_growth = [4, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 18, 20, 21]
hydro_growth = [3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9]
geo_growth = [2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8]
bio_growth = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7]

# Consistent color for all plots
consistent_color = '#32CD32'

# Create the figure and set up two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First Plot: Pie Chart
ax1.pie(
    usage_percentages,
    labels=energy_sources,
    colors=[consistent_color] * len(energy_sources),
    autopct='%1.1f%%',
    startangle=140,
    shadow=True
)

# Set the title
ax1.set_title("Global Renewable Energy Usage Distribution 2023", fontsize=16, fontweight='bold', pad=20)

# Ensure the pie chart is circular
ax1.axis('equal')

# Second Plot: Line Chart for Annual Growth
ax2.plot(years, solar_growth, marker='o', linestyle='-', linewidth=2, color=consistent_color, label='Solar')
ax2.plot(years, wind_growth, marker='s', linestyle='--', linewidth=2, color=consistent_color, label='Wind')
ax2.plot(years, hydro_growth, marker='^', linestyle='-.', linewidth=2, color=consistent_color, label='Hydropower')
ax2.plot(years, geo_growth, marker='d', linestyle=':', linewidth=2, color=consistent_color, label='Geothermal')
ax2.plot(years, bio_growth, marker='x', linestyle='-', linewidth=2, color=consistent_color, label='Biomass')

# Customize the chart
ax2.set_title("Annual Growth of Renewable Energy Sources (2010-2023)", fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel("Year", fontsize=14)
ax2.set_ylabel("Growth Rate (%)", fontsize=14)
ax2.set_xticks(years)
ax2.set_xlim(2010, 2023)
ax2.set_ylim(0, 30)
ax2.legend(title="Energy Sources", loc="upper left", fontsize=10, title_fontsize='13')
ax2.grid(True, linestyle='--', alpha=0.5)

# Make the layout tight to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()