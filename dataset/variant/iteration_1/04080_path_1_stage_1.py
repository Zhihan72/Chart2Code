import matplotlib.pyplot as plt
import numpy as np

# Departments
departments = ['Resources', 'Programs & Events', 'Technology', 'Staff Development', 'Maintenance']

# Budget allocations (in millions USD) from 2017 to 2021
budget_2017 = [4.5, 2.5, 3.8, 1.8, 2.0]
budget_2018 = [4.8, 2.7, 4.1, 1.9, 2.1]
budget_2019 = [5.0, 2.8, 4.5, 2.0, 2.2]
budget_2020 = [5.3, 3.0, 4.6, 2.3, 2.3]
budget_2021 = [5.5, 3.2, 4.8, 2.5, 2.4]

# Combine the data into a numpy array for easier plotting
data = np.array([budget_2017, budget_2018, budget_2019, budget_2020, budget_2021])

# Set up the bar chart
fig, ax = plt.subplots(figsize=(14, 8))

# Define the positions of the bars
x = np.arange(len(departments))
width = 0.15

# Plotting bars for each year
for i in range(data.shape[0]):
    ax.bar(x + (i - 2) * width, data[i], width, edgecolor='black')

# Adding labels and title
ax.set_xlabel('Library Departments', fontsize=14)
ax.set_ylabel('Budget Allocation (in Millions USD)', fontsize=14)
ax.set_title('Yearly Library Budget Allocation Across Departments (2017-2021)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(departments, rotation=30, ha='right')

# Remove grid and legend
ax.yaxis.grid(False)
ax.legend().remove()

# Annotate bars with their values
for i in range(data.shape[0]):
    bars = ax.bar(x + (i - 2) * width, data[i], width)
    for bar, height in zip(bars, data[i]):
        ax.annotate(f'{height:.1f}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='black')

# Automatically adjust layout
plt.tight_layout()

# Display the bar chart
plt.show()