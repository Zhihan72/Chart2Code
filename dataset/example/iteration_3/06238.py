import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of a Tech Company's Operating Expenditure in 2023
# The company aims to gain insights into how its budget is allocated across various departments.

# Define the departments and their respective expenditure in millions
departments = ['R&D', 'Marketing', 'Sales', 'HR', 'IT', 'Operations']
expenditure = [45, 20, 15, 10, 7, 3]  # in millions

# Define colors for each slice
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF', '#FFD700']

# Explode the slice for R&D to emphasize it
explode = (0.1, 0, 0, 0, 0, 0)

# Annual growth rates of expenditure for each department (%) for a secondary subplot
growth_rates = [8, 12, 5, 7, 9, 3]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

# Pie chart on the left
wedges, texts, autotexts = ax1.pie(
    expenditure, explode=explode, labels=departments, colors=colors, autopct='%1.1f%%',
    startangle=140, shadow=True, wedgeprops=dict(edgecolor='black', linewidth=1.5))

# Enhance text properties
plt.setp(autotexts, size=10, weight="bold", color="black")

# Set title for the pie chart
ax1.set_title('2023 Operating Expenditure by Department (in Millions)', fontsize=14, fontweight='bold', pad=20)
ax1.legend(title='Departments', loc='upper right', bbox_to_anchor=(1.3, 0.8), shadow=True, fontsize=10)

# Bar chart on the right to show annual growth rates
y_pos = np.arange(len(departments))
ax2.barh(y_pos, growth_rates, color=colors, edgecolor='black')

# Set properties for the bar chart
ax2.set_yticks(y_pos)
ax2.set_yticklabels(departments)
ax2.invert_yaxis()  # Highest growth rate on top
ax2.set_xlabel('Annual Growth Rate (%)', fontsize=12)
ax2.set_title('Annual Growth Rates of Departmental Expenditure', fontsize=14, fontweight='bold', pad=20)

# Annotate growth rates on the bars
for i, v in enumerate(growth_rates):
    ax2.text(v + 0.3, i, f"{v}%", color='black', va='center', fontweight='bold')

# Automatically adjust layout to ensure no overlap
plt.tight_layout()

# Display the plots
plt.show()