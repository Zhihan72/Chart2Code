import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart visualizes the growth of a hypothetical software company over several years.
# The company has been progressively increasing its market share and revenue while also investing in research & development and employee growth.

# Define the years and corresponding values for different metrics
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
market_share = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
revenue = np.array([1, 2, 3.5, 5, 7.5, 10, 13.5, 17, 22])
rnd_investment = np.array([0.2, 0.5, 0.8, 1.2, 1.8, 2.5, 4, 5.5, 7])
employee_growth = np.array([50, 60, 80, 110, 150, 200, 270, 350, 450])

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot area charts for different metrics
ax.fill_between(years, market_share, color='skyblue', alpha=0.6, label='Market Share (%)')
ax.fill_between(years, revenue, color='lightgreen', alpha=0.6, label='Revenue (millions)')
ax.fill_between(years, rnd_investment, color='lightcoral', alpha=0.6, label='R&D Investment (millions)')
ax.fill_between(years, employee_growth, color='wheat', alpha=0.6, label='Employee Growth (count)')

# Title and labels with contextual information
ax.set_title('Growth Metrics of Imaginary Software Company (2015-2023)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Values', fontsize=14)

# Add legend with context-specific descriptions
ax.legend(loc='upper left', fontsize=12, title='Metrics', title_fontsize='13')

# Add grids to the plot for better readability
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate critical points on the charts
ax.annotate('Start-up Phase', xy=(2015, market_share[0]), xytext=(2016.5, 15),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black')

ax.annotate('Revenue Surge', xy=(2020, revenue[5]), xytext=(2021.5, 18),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black')

ax.annotate('Major R&D Boost', xy=(2022, rnd_investment[7]), xytext=(2023, 9),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black')

ax.annotate('Significant Employee Growth', xy=(2023, employee_growth[8]), xytext=(2020, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='black')

# Automatically adjust layout to prevent text overlapping
plt.tight_layout()

# Display the plot
plt.show()