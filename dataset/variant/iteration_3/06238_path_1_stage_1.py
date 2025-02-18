import matplotlib.pyplot as plt

# Define the departments and their respective expenditure in millions
departments = ['R&D', 'Marketing', 'Sales', 'HR', 'IT', 'Operations']
expenditure = [45, 20, 15, 10, 7, 3]  # in millions

# Define colors for each slice
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CC99FF', '#FFD700']

# Explode the slice for R&D to emphasize it
explode = (0.1, 0, 0, 0, 0, 0)

# Create a single subplot for the pie chart
fig, ax1 = plt.subplots(figsize=(8, 8))

# Pie chart
wedges, texts, autotexts = ax1.pie(
    expenditure, explode=explode, labels=departments, colors=colors, autopct='%1.1f%%',
    startangle=140, shadow=True, wedgeprops=dict(edgecolor='black', linewidth=1.5))

# Enhance text properties
plt.setp(autotexts, size=10, weight="bold", color="black")

# Set title for the pie chart
ax1.set_title('2023 Operating Expenditure by Department (in Millions)', fontsize=14, fontweight='bold', pad=20)
ax1.legend(title='Departments', loc='upper right', bbox_to_anchor=(1.3, 0.8), shadow=True, fontsize=10)

# Automatically adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()