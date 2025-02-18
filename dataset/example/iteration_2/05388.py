import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the Average Temperature Trends During the Summer Months (June - August)
# for Different Cities Over the Last Decade (2010-2020)

# Cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Years
years = np.arange(2010, 2021)

# Average temperatures in Fahrenheit (hypothetical data)
ny_temps = [74, 75, 76, 77, 78, 79, 80, 81, 82, 82, 83]
la_temps = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]
chi_temps = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
hou_temps = [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]
phx_temps = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature trends
ax.plot(years, ny_temps, marker='o', label='New York', color='#1f77b4', linewidth=2)
ax.plot(years, la_temps, marker='s', label='Los Angeles', color='#ff7f0e', linewidth=2)
ax.plot(years, chi_temps, marker='^', label='Chicago', color='#2ca02c', linewidth=2)
ax.plot(years, hou_temps, marker='d', label='Houston', color='#d62728', linewidth=2)
ax.plot(years, phx_temps, marker='p', label='Phoenix', color='#9467bd', linewidth=2)

# Title and axis labels
ax.set_title("Summer Heat Analysis: Average Temperature Trends (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Temperature (°F)', fontsize=12)

# Annotate key temperature increases
ax.annotate('Significant rise in temperature', xy=(2016, 81), xytext=(2013, 77),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

ax.annotate('LA surpasses 80°F', xy=(2019, 80), xytext=(2018, 75),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

# Label each data point with its value
for idx, year in enumerate(years):
    ax.text(year, ny_temps[idx] + 0.5, f'{ny_temps[idx]}°F', ha='center', va='bottom', fontsize=9)
    ax.text(year, la_temps[idx] + 0.5, f'{la_temps[idx]}°F', ha='center', va='bottom', fontsize=9)
    ax.text(year, chi_temps[idx] + 0.5, f'{chi_temps[idx]}°F', ha='center', va='bottom', fontsize=9)
    ax.text(year, hou_temps[idx] + 0.5, f'{hou_temps[idx]}°F', ha='center', va='bottom', fontsize=9)
    ax.text(year, phx_temps[idx] + 0.5, f'{phx_temps[idx]}°F', ha='center', va='bottom', fontsize=9)

# Add a legend
ax.legend(loc='upper left', fontsize=10)

# Enable grid
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()