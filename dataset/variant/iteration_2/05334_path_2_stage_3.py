import matplotlib.pyplot as plt
import numpy as np

# Define years and categories
years = np.array([2018, 2019, 2020, 2021, 2022])
categories = ['IT Infrastructure', 'Marketing', 'Research & Development', 'Miscellaneous', 
              'Salaries', 'Operational Costs', 'Training & Development']

# Define the budget allocation data for each department (in millions)
data = np.array([
    [8, 10, 12, 14, 16],        # IT Infrastructure
    [20, 25, 30, 35, 40],       # Marketing
    [15, 20, 25, 30, 35],       # Research & Development
    [5, 6, 7, 8, 9],            # Miscellaneous
    [50, 55, 60, 65, 70],       # Salaries
    [10, 15, 20, 25, 30],       # Operational Costs
    [3, 4, 5, 6, 7]             # Training & Development
])

# Order categories based on changed indices
sorted_indices = [5, 1, 2, 4, 0, 3, 6]

# Reorder data and categories
data = data[sorted_indices]
categories = np.array(categories)[sorted_indices]

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for the year 2022
ax.bar(categories, data[:, -1], color=['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', 
                                       '#ffff33', '#a65628'], edgecolor='k', linewidth=0.6)

# Set titles and labels
ax.set_title("Financial Plan Distribution for 2022 (Rearranged Groups)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sections", fontsize=14)
ax.set_ylabel("Funding Allocations (millions)", fontsize=14)

# Display values on the bars
for i, value in enumerate(data[:, -1]):
    ax.text(i, value / 2, f'{value}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display plot
plt.show()