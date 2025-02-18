import matplotlib.pyplot as plt
import numpy as np

# Data setup for diverging bar chart
cities = ['New York', 'Los Angeles', 'Chicago']
utilities = ['Electricity', 'Water', 'Internet']

# Average monthly costs (in USD)
electricity_cost = [150, 135, 145]
water_cost = [50, 55, 45]
internet_cost = [70, 65, 75]

# Combine data for stack plotting
positive_data = np.array([electricity_cost, water_cost, internet_cost])
negative_data = -1 * positive_data

# Bar width and positions
index = np.arange(len(cities))

# Colors for each utility
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each utility's data diverging from the center
for i, (utility, color) in enumerate(zip(utilities, colors)):
    ax.bar(index, positive_data[i], 0.5, label=utility + ' (Above)', color=color)
    ax.bar(index, negative_data[i], 0.5, color=color, alpha=0.5)

# Labels, title, and legend
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Average Monthly Cost (USD)', fontsize=12)
ax.set_title('Diverging Bar Chart of Utility Costs in Major Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xticks(index)
ax.set_xticklabels(cities)

# Adding value labels on bars
for i in range(len(utilities)):
    for j in range(len(cities)):
        ax.text(index[j], positive_data[i][j] + 2, 
                f'${positive_data[i][j]:.0f}', ha='center', va='bottom', fontsize=10)
        ax.text(index[j], negative_data[i][j] - 5, 
                f'${-negative_data[i][j]:.0f}', ha='center', va='top', fontsize=10, alpha=0.5)

# Adding legend
ax.legend(title='Utilities', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Central axis
ax.axhline(0, color='black', linewidth=0.8)

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()