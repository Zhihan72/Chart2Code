import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of Average Monthly Costs of Different Utility Services Across Three Major Cities in 2023
# Cities: New York, Los Angeles, Chicago
# Utilities: Electricity, Water, Internet

# Define the data
cities = ['New York', 'Los Angeles', 'Chicago']
utilities = ['Electricity', 'Water', 'Internet']

# Average monthly costs (in USD)
electricity_cost = [150, 135, 145]
water_cost = [50, 55, 45]
internet_cost = [70, 65, 75]

# Combining utilities for grouped bar chart
data = np.array([electricity_cost, water_cost, internet_cost])

# Bar width and positions
bar_width = 0.25
index = np.arange(len(cities))

# Colors for each utility
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each utility's data
for i, (utility, color) in enumerate(zip(utilities, colors)):
    ax.bar(index + i * bar_width, data[i], bar_width, label=utility, color=color)

# Labels, title, and legend
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Average Monthly Cost (USD)', fontsize=12)
ax.set_title('Average Monthly Costs of Utility Services in Major Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(cities)

# Adding value labels on bars
for i in range(len(utilities)):
    for j in range(len(cities)):
        ax.text(index[j] + i * bar_width, data[i][j] + 2, 
                f'${data[i][j]:.0f}', ha='center', va='bottom', fontsize=10)

# Adding legend
ax.legend(title='Utilities', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Automatic layout adjustment
plt.tight_layout()

# Display the plot
plt.show()