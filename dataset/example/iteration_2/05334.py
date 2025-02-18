import matplotlib.pyplot as plt
import numpy as np

# Define years and categories
years = np.array([2018, 2019, 2020, 2021, 2022])
categories = ['Salaries', 'Marketing', 'Research & Development', 'Operational Costs', 'Miscellaneous']

# Define the budget allocation data for each department (in millions)
salaries = np.array([50, 55, 60, 65, 70])
marketing = np.array([20, 25, 30, 35, 40])
research = np.array([15, 20, 25, 30, 35])
operational = np.array([10, 15, 20, 25, 30])
miscellaneous = np.array([5, 6, 7, 8, 9])

# Stack the data
data = np.vstack([salaries, marketing, research, operational, miscellaneous])

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define bottom array for stacking
bottom = np.zeros(len(years))

# Define color palette
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c']

# Plot each category's data on top of the previous stack
for i, (datum, color) in enumerate(zip(data, colors)):
    ax.bar(years, datum, bottom=bottom, label=categories[i], color=color, edgecolor='k', linewidth=0.6)
    bottom += datum

# Set titles and labels
ax.set_title("Company Budget Allocation Over Five Years\n(2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Budget Allocation (in millions)", fontsize=14)

# Add a legend
ax.legend(title="Departments", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Customize y-axis limits
ax.set_ylim(0, 200)

# Display values on the bars
for year_index, year in enumerate(years):
    y_offset = 0
    for value_index, category in enumerate(categories):
        val = data[value_index, year_index]
        ax.text(year, y_offset + val / 2, f'{val}', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
        y_offset += val

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()