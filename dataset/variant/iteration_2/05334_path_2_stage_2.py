import matplotlib.pyplot as plt
import numpy as np

# Define years and categories
years = np.array([2018, 2019, 2020, 2021, 2022])
categories = ['Salaries', 'Marketing', 'Research & Development', 'Operational Costs', 
              'Miscellaneous', 'IT Infrastructure', 'Training & Development']

# Define the budget allocation data for each department (in millions)
data = np.array([
    [50, 55, 60, 65, 70],       # Salaries
    [20, 25, 30, 35, 40],       # Marketing
    [15, 20, 25, 30, 35],       # Research & Development
    [10, 15, 20, 25, 30],       # Operational Costs
    [5, 6, 7, 8, 9],            # Miscellaneous
    [8, 10, 12, 14, 16],        # IT Infrastructure
    [3, 4, 5, 6, 7]             # Training & Development
])

# Sorting categories based on 2022 values for descending order as an example
sorted_indices = np.argsort(data[:, -1])[::-1]

# Reordering data and categories
data = data[sorted_indices]
categories = np.array(categories)[sorted_indices]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for the year 2022 as an example (can be modified for other years)
ax.bar(categories, data[:, -1], color=['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', 
                                       '#ffff33', '#a65628'], edgecolor='k', linewidth=0.6)

# Set titles and labels
ax.set_title("Company Budget Allocation for 2022 (Sorted by Department)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Departments", fontsize=14)
ax.set_ylabel("Budget Allocation (in millions)", fontsize=14)

# Display values on the bars
for i, value in enumerate(data[:, -1]):
    ax.text(i, value / 2, f'{value}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Add a grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()