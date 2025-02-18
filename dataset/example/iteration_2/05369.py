import matplotlib.pyplot as plt
import numpy as np

# Backstory: Growth of Solar Energy Generation Over a Decade
# Data represents solar energy generation (in gigawatts) in different regions over the period 2010 to 2020.
years = np.arange(2010, 2021)

# Solar energy generation data (in gigawatts) for different regions
asia = [45, 50, 58, 65, 70, 80, 95, 110, 130, 150, 170]
europe = [30, 35, 40, 48, 55, 65, 75, 85, 95, 107, 120]
north_america = [25, 28, 35, 44, 50, 60, 70, 82, 95, 110, 125]
oceania = [5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 55]

# Create the line chart
plt.figure(figsize=(14, 8))

# Plotting each region's data
plt.plot(years, asia, marker='o', linestyle='-', color='orange', label='Asia', linewidth=2)
plt.plot(years, europe, marker='s', linestyle='--', color='blue', label='Europe', linewidth=2)
plt.plot(years, north_america, marker='^', linestyle='-.', color='green', label='North America', linewidth=2)
plt.plot(years, oceania, marker='D', linestyle=':', color='purple', label='Oceania', linewidth=2)

# Customizing the chart
plt.title("Decade of Solar Energy Generation Growth\n(2010-2020)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Solar Generation (Gigawatts)", fontsize=14)
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(np.arange(0, 201, 20), fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Regions', loc='upper left', fontsize=12)

# Annotate peak generation for each region
for region, data, color in zip(['Asia', 'Europe', 'North America', 'Oceania'],
                               [asia, europe, north_america, oceania],
                               ['orange', 'blue', 'green', 'purple']):
    max_gen = max(data)
    max_year = years[data.index(max_gen)]
    plt.annotate(f'Peak: {max_gen} GW', xy=(max_year, max_gen),
                 xytext=(max_year - 0.5, max_gen + 5),
                 arrowprops=dict(facecolor=color, arrowstyle='->'),
                 fontsize=10, color=color)

# Enhance the layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()