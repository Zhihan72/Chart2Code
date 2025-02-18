import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# The chart will showcase the productivity levels of different departments in a tech company over four quarters. The aim is to understand how each department performs throughout the year and identify areas for improvement.

# Data Construction:
departments = ["Development", "Marketing", "Sales", "HR", "Customer Support", "R&D"]
quarters = ["Q1", "Q2", "Q3", "Q4"]

# Productivity data in percentage (values between 0 to 100)
development = [85, 88, 90, 87]
marketing = [70, 75, 80, 78]
sales = [90, 92, 89, 88]
hr = [65, 70, 68, 72]
customer_support = [88, 85, 87, 90]
rnd = [95, 97, 98, 96]

# Create a numpy array to manage the data
productivity_data = np.array([development, marketing, sales, hr, customer_support, rnd])

# Plotting the Bar Chart
fig, ax = plt.subplots(figsize=(14, 8))

# X-axis locations for the groups
x = np.arange(len(quarters))

# Width of the bars
bar_width = 0.13

# Define color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot bars for each department
for i, department in enumerate(departments):
    ax.bar(x + i * bar_width, productivity_data[i], bar_width, label=department, color=colors[i])

# Adding labels, title, and customizing
ax.set_title("Quarterly Productivity Levels of Tech Company Departments (2023)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Quarters', fontsize=12)
ax.set_ylabel('Productivity (%)', fontsize=12)
ax.set_xticks(x + bar_width * (len(departments) - 1) / 2)
ax.set_xticklabels(quarters)
ax.set_ylim(0, 110)

# Adding value labels on top of bars
for i in range(len(departments)):
    for j in range(len(quarters)):
        ax.text(x[j] + i * bar_width, productivity_data[i, j] + 1, f"{productivity_data[i, j]}%", ha='center', va='bottom', fontsize=9, fontweight='bold')

# Customize and position the legend
ax.legend(
    loc='upper left', 
    bbox_to_anchor=(1, 1), 
    title="Departments", 
    fontsize=10
)

# Grid to improve readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()