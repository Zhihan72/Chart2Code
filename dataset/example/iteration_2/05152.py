import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking monthly utility bills for different house sizes in a suburban neighborhood in 2023.
# The chart will show bar plots for utility bills: electricity, water, and gas for small, medium, and large homes.

# Define the months and house sizes
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
house_sizes = ["Small", "Medium", "Large"]

# Monthly utility bills data (in dollars)
electricity_bills = np.array([
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],  # Small
    [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],  # Medium
    [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175],  # Large
])

water_bills = np.array([
    [20, 22, 24, 25, 28, 30, 31, 33, 35, 36, 38, 40],  # Small
    [30, 32, 34, 35, 37, 39, 41, 43, 45, 47, 48, 50],  # Medium
    [40, 42, 44, 46, 48, 50, 51, 53, 55, 57, 58, 60],  # Large
])

gas_bills = np.array([
    [25, 26, 27, 30, 31, 32, 33, 35, 36, 38, 39, 40],  # Small
    [35, 36, 38, 40, 42, 44, 45, 47, 49, 50, 52, 54],  # Medium
    [45, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66],  # Large
])

# Plotting the stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot utility bills for Small homes
bar_width = 0.2
x = np.arange(len(months))

ax.bar(x - bar_width, electricity_bills[0], width=bar_width, label='Electricity (Small)', color='#4CAF50')
ax.bar(x - bar_width, water_bills[0], width=bar_width, bottom=electricity_bills[0], color='#2196F3')
ax.bar(x - bar_width, gas_bills[0], width=bar_width, bottom=electricity_bills[0] + water_bills[0], color='#FFC107')

# Plot utility bills for Medium homes
ax.bar(x, electricity_bills[1], width=bar_width, label='Electricity (Medium)', color='#8BC34A')
ax.bar(x, water_bills[1], width=bar_width, bottom=electricity_bills[1], color='#03A9F4')
ax.bar(x, gas_bills[1], width=bar_width, bottom=electricity_bills[1] + water_bills[1], color='#FFEB3B')

# Plot utility bills for Large homes
ax.bar(x + bar_width, electricity_bills[2], width=bar_width, label='Electricity (Large)', color='#388E3C')
ax.bar(x + bar_width, water_bills[2], width=bar_width, bottom=electricity_bills[2], color='#0288D1')
ax.bar(x + bar_width, gas_bills[2], width=bar_width, bottom=electricity_bills[2] + water_bills[2], color='#FFC107')

# Set chart title and labels
ax.set_title("Monthly Utility Bills for Different House Sizes in 2023\nSuburban Neighborhood", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Utility Bills (in dollars)", fontsize=12)

# Set x-ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(months)

# Add legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Utility Type (House Size)')

# Add gridlines for easier reading
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()