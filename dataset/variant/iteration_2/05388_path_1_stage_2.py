import matplotlib.pyplot as plt
import numpy as np

# Cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Years
years = np.arange(2010, 2021)

# Average temperatures in Fahrenheit (altered data)
ny_temps = [82, 79, 80, 78, 81, 74, 83, 76, 75, 82, 77]
la_temps = [79, 76, 80, 78, 81, 72, 82, 75, 77, 74, 73]
chi_temps = [71, 78, 72, 79, 80, 76, 77, 75, 74, 73, 70]
hou_temps = [85, 90, 86, 91, 89, 92, 87, 94, 88, 84, 93]
phx_temps = [108, 102, 106, 110, 104, 100, 107, 101, 105, 109, 103]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the temperature trends with shuffled colors
ax.plot(years, ny_temps, marker='o', label='New York', color='#9467bd', linewidth=2)
ax.plot(years, la_temps, marker='s', label='Los Angeles', color='#1f77b4', linewidth=2)
ax.plot(years, chi_temps, marker='^', label='Chicago', color='#d62728', linewidth=2)
ax.plot(years, hou_temps, marker='d', label='Houston', color='#ff7f0e', linewidth=2)
ax.plot(years, phx_temps, marker='p', label='Phoenix', color='#2ca02c', linewidth=2)

# Title and axis labels
ax.set_title("Summer Heat Analysis: Average Temperature Trends (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Average Temperature (°F)', fontsize=12)

# Annotate key temperature increases
ax.annotate('Significant rise in temperature', xy=(2016, 79), xytext=(2013, 82),
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