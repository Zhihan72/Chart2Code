import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory:
# The chart represents a nationwide initiative to promote community gardening and self-sustainability in urban areas.
# We compare the number of gardens set up in different cities over the past five years and the total harvest yield in kilograms from these gardens.

# Define cities and years
cities = ['Springfield', 'Shelbyville', 'Ogdenville', 'North Haverbrook', 'Capital City']
years = ['2019', '2020', '2021', '2022', '2023']

# Data: Number of gardens set up each year in each city
gardens_setup = np.array([
    [12, 15, 19, 20, 24],  # Springfield
    [10, 12, 15, 18, 22],  # Shelbyville
    [7, 10, 13, 15, 20],   # Ogdenville
    [5, 8, 10, 12, 16],    # North Haverbrook
    [14, 18, 21, 22, 25]   # Capital City
])

# Data: Harvest yield in kilograms for each city each year
harvest_yield = np.array([
    [1200, 1350, 1500, 1600, 1800],  # Springfield
    [1100, 1225, 1375, 1475, 1600],  # Shelbyville
    [700, 900, 1000, 1100, 1250],    # Ogdenville
    [500, 750, 850, 950, 1100],      # North Haverbrook
    [1400, 1500, 1600, 1700, 1800]   # Capital City
])

# Aggregate data for the second subplot
total_harvest_yield = harvest_yield.sum(axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

# Subplot 1: Stacked bar chart for gardens setup
bottoms = np.zeros(len(cities))
for i, year in enumerate(years):
    bars = ax1.bar(cities, gardens_setup[:, i], bottom=bottoms, label=year)
    bottoms += gardens_setup[:, i]
    
    # Annotate each bar with data label (number of gardens)
    for bar in bars:
        height = bar.get_height()
        if height > 5:  # Only annotate if the height is greater than a threshold
            ax1.annotate(f'{int(height)}', 
                         xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                         xytext=(0, 0), textcoords="offset points",
                         ha='center', va='center', fontsize=8, color='white')

ax1.set_title("Community Gardens Setup in Urban Centers (2019-2023)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Cities", fontsize=12)
ax1.set_ylabel("Number of Gardens Setup", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.legend(title="Year", title_fontsize='11', fontsize='10', loc='upper left')

# Subplot 2: Bar chart for total harvest yield
bars = ax2.bar(cities, total_harvest_yield, color='darkgreen', alpha=0.7)

# Annotate bars with harvest yield values
for bar, yield_amount in zip(bars, total_harvest_yield):
    ax2.annotate(f'{yield_amount} kg', 
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                 xytext=(0, 5), textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, color='black')

ax2.set_title("Total Harvest Yield from Community Gardens (2019-2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Cities", fontsize=12)
ax2.set_ylabel("Harvest Yield (kg)", fontsize=12)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)

# Set layout adjustments and display the plot
fig.suptitle("Community Gardening Initiatives Over Five Years", fontsize=18, fontweight='bold', y=1.02)
plt.show()