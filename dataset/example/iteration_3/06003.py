import matplotlib.pyplot as plt
import numpy as np

# Backstory: "Annual Budget Allocation for City Departments"
# The city council of Metropolis needs to convey its budget allocation plans for various city departments in 2023.
# This plot shows the distribution and comparison of the budget allocated to different departments over the years 2020 to 2022.
years = ['2020', '2021', '2022']
departments = ['Health', 'Education', 'Infrastructure', 'Public Safety', 'Arts & Culture']
budget_2020 = [150, 180, 210, 170, 60]
budget_2021 = [155, 190, 220, 180, 65]
budget_2022 = [160, 200, 230, 190, 70]

# Position of bars on x-axis
x = np.arange(len(departments))

# Width of a bar
width = 0.25

# Create a figure and three subplots to compare budgets over the years
fig, ax = plt.subplots(figsize=(14, 8))

# Bar charts for each year
bars_2020 = ax.bar(x - width, budget_2020, width, label='2020', color='skyblue')
bars_2021 = ax.bar(x, budget_2021, width, label='2021', color='lightgreen')
bars_2022 = ax.bar(x + width, budget_2022, width, label='2022', color='lightcoral')

# Customization of the plot
ax.set_title('Annual Budget Allocation for City Departments (2020-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Departments', fontsize=12)
ax.set_ylabel('Budget in Millions (USD)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(departments)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(title='Year', fontsize=10)

# Annotate each bar with corresponding budget values
def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

add_labels(ax, bars_2020)
add_labels(ax, bars_2021)
add_labels(ax, bars_2022)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()