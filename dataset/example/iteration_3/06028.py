import matplotlib.pyplot as plt
import numpy as np

# Backstory: The population change of three fictitious cities over a decade (2010-2020).
# Titles emphasize urban planning efforts, labels, and legends detail the data.

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Population data for three cities in millions
city1_population = [1.2, 1.25, 1.32, 1.40, 1.45, 1.50, 1.55, 1.60, 1.70, 1.75, 1.80]
city2_population = [0.8, 0.85, 0.88, 0.92, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25]
city3_population = [0.5, 0.55, 0.58, 0.65, 0.72, 0.78, 0.82, 0.85, 0.90, 0.95, 1.00]

# Calculate annual growth rate for each city
def calculate_annual_growth_rate(data):
    return [100 * (data[k+1] - data[k]) / data[k] for k in range(len(data)-1)]

city1_growth = calculate_annual_growth_rate(city1_population)
city2_growth = calculate_annual_growth_rate(city2_population)
city3_growth = calculate_annual_growth_rate(city3_population)

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot the population line chart
ax1.plot(years, city1_population, marker='o', linestyle='-', color='blue', linewidth=2, label='City Alpha')
ax1.plot(years, city2_population, marker='s', linestyle='--', color='green', linewidth=2, label='City Beta')
ax1.plot(years, city3_population, marker='^', linestyle='-.', color='red', linewidth=2, label='City Gamma')
ax1.set_title("Urban Growth Analysis:\nTracking Population Changes (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Population (Millions)', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.axvspan(2014, 2016, color='yellow', alpha=0.3, label='Urban Planning Initiative')
ax1.annotate('Planning Initiative', xy=(2015, 1.55), xytext=(2013, 1.75),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
             fontsize=10, color='black')

# Plot the bar chart for annual growth rate
ind = np.arange(len(city1_growth))  # index for bar positions
width = 0.25  # bar width

ax2.bar(ind - width, city1_growth, width=width, color='blue', alpha=0.7, label='City Alpha')
ax2.bar(ind, city2_growth, width=width, color='green', alpha=0.7, label='City Beta')
ax2.bar(ind + width, city3_growth, width=width, color='red', alpha=0.7, label='City Gamma')
ax2.set_title('Annual Population Growth Rate', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Growth Rate (%)', fontsize=12, fontweight='bold')
ax2.set_xticks(ind)
ax2.set_xticklabels(years[1:])  # exclude the first year since growth rate is computed from the second year onwards
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()