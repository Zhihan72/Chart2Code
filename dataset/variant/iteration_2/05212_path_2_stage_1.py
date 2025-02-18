import matplotlib.pyplot as plt
import numpy as np

# Define countries and years
countries = ['Norway', 'Germany', 'USA', 'Australia', 'India', 'Brazil']
years = ['2018', '2019', '2020', '2021', '2022']

# Renewable energy production in Gigawatt-hours (GWh)
norway_production = [50000, 51000, 52000, 53000, 55000]
germany_production = [200000, 210000, 220000, 230000, 250000]
usa_production = [300000, 315000, 320000, 335000, 360000]
australia_production = [150000, 160000, 170000, 180000, 195000]
india_production = [100000, 110000, 120000, 130000, 150000]
brazil_production = [80000, 85000, 90000, 95000, 100000]  # New data series

# Aggregate data for plotting
data = [norway_production, germany_production, usa_production, australia_production, india_production, brazil_production]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting details
width = 0.13  # reduced width for inclusion of additional dataset
x = np.arange(len(years))  # the label locations

# Colors for each country
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']  # Added new color

# Plot each country's data as a separate set of bars
for i, (country_data, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, country_data, width, label=countries[i], color=color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

# Customizing the plot
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Renewable Energy Production (GWh)', fontsize=12)
ax.set_title('Annual Renewable Energy Production\n(2018-2022)', fontsize=18, fontweight='bold', pad=20)
ax.set_xticks(x + width * 2.5)  # Adjusted for new data
ax.set_xticklabels(years, fontsize=11)
ax.legend(title="Country", fontsize=10, loc='upper left')

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()