import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Population data for two cities in millions
city1_population = [1.2, 1.25, 1.32, 1.40, 1.45, 1.50, 1.55, 1.60, 1.70, 1.75, 1.80]
city2_population = [0.8, 0.85, 0.88, 0.92, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25]

# Calculate annual growth rate for each city
def calculate_annual_growth_rate(data):
    return [100 * (data[k+1] - data[k]) / data[k] for k in range(len(data)-1)]

city1_growth = calculate_annual_growth_rate(city1_population)
city2_growth = calculate_annual_growth_rate(city2_population)

# Set up the subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot the population line chart
ax1.plot(years, city1_population, marker='o', linestyle='-', color='blue', linewidth=2, label='Metropolis A')
ax1.plot(years, city2_population, marker='s', linestyle='--', color='green', linewidth=2, label='Urban Zone B')
ax1.set_title("Population Dynamics:\nAn Overview from 2010 to 2020", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Timeline', fontsize=12, fontweight='bold')
ax1.set_ylabel('Residents (Millions)', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax1.legend(loc='upper left', fontsize=10)
ax1.axvspan(2014, 2016, color='yellow', alpha=0.3, label='Development Era')
ax1.annotate('Growth Initiative', xy=(2015, 1.55), xytext=(2013, 1.75),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black'),
             fontsize=10, color='black')

# Plot the bar chart for annual growth rate
ind = np.arange(len(city1_growth))  # index for bar positions
width = 0.3  # adjusted bar width for two bars

ax2.bar(ind - width/2, city1_growth, width=width, color='blue', alpha=0.7, label='Metropolis A')
ax2.bar(ind + width/2, city2_growth, width=width, color='green', alpha=0.7, label='Urban Zone B')
ax2.set_title('Yearly Growth Trends', fontsize=14, fontweight='bold', pad=10)
ax2.set_xlabel('Timeline', fontsize=12, fontweight='bold')
ax2.set_ylabel('Growth Percentage', fontsize=12, fontweight='bold')
ax2.set_xticks(ind)
ax2.set_xticklabels(years[1:])
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()