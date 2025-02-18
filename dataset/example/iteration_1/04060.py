import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart represents the distribution of various types of renewable energy usage globally in 2023.
# The second subplot shows the trend of annual growth of these renewable resources from 2010 to 2023.

# Pie chart data: Renewable energy sources and their usage percentages
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Geothermal', 'Biomass']
usage_percentages = [30, 25, 20, 15, 10]

# Subplot data: Annual growth data for each energy source (in percentage)
years = np.arange(2010, 2024)
solar_growth = [5, 7, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 25, 26]  # Example data
wind_growth = [4, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 18, 20, 21]
hydro_growth = [3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9]
geo_growth = [2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8]
bio_growth = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7]

# Colors for the pie chart
colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF8C00', '#8B4513']

# Create the figure and set up two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --- First Plot: Pie Chart ---
wedges, texts, autotexts = ax1.pie(
    usage_percentages,
    labels=energy_sources,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True
)

# Customize the autotexts for better visibility
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Set the title
ax1.set_title("Global Renewable Energy Usage Distribution 2023", fontsize=16, fontweight='bold', pad=20)

# Ensure the pie chart is circular
ax1.axis('equal')

# --- Second Plot: Line Chart for Annual Growth ---
ax2.plot(years, solar_growth, marker='o', linestyle='-', linewidth=2, color='#FFD700', label='Solar')
ax2.plot(years, wind_growth, marker='s', linestyle='--', linewidth=2, color='#87CEEB', label='Wind')
ax2.plot(years, hydro_growth, marker='^', linestyle='-.', linewidth=2, color='#32CD32', label='Hydropower')
ax2.plot(years, geo_growth, marker='d', linestyle=':', linewidth=2, color='#FF8C00', label='Geothermal')
ax2.plot(years, bio_growth, marker='x', linestyle='-', linewidth=2, color='#8B4513', label='Biomass')

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