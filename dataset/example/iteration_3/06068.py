import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the productivity trends of three departments over a period of one year at a tech company.
# Each department's monthly productivity (in arbitrary units) is tracked and displayed.

# Define the months and departments
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
departments = ['Development', 'Marketing', 'Sales']

# Productivity data explicitly constructed
prod_development = [i * 1.5 for i in [10, 13, 8, 15, 20, 18, 25, 22, 19, 25, 30, 28]]
prod_marketing = [i * 1.4 for i in [12, 10, 15, 11, 18, 17, 19, 25, 23, 21, 26, 24]]
prod_sales = [i * 1.6 for i in [14, 18, 16, 20, 24, 22, 26, 30, 28, 27, 32, 30]]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data for each department
ax.plot(months, prod_development, marker='o', linestyle='-', color='blue', label='Development Dept.')
ax.plot(months, prod_marketing, marker='s', linestyle='--', color='green', label='Marketing Dept.')
ax.plot(months, prod_sales, marker='^', linestyle=':', color='red', label='Sales Dept.')

# Set the title, labels, and legend
ax.set_title('Monthly Productivity Trends in a Tech Company (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Productivity Units', fontsize=12)
ax.set_xlabel('Months', fontsize=12)
ax.legend(title='Departments', fontsize=12, loc='upper left')

# Adding grid and customizing it
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate key points
for i, month in enumerate(months):
    ax.annotate(f"{prod_development[i]} u", (month, prod_development[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='blue')
    ax.annotate(f"{prod_marketing[i]} u", (month, prod_marketing[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='green')
    ax.annotate(f"{prod_sales[i]} u", (month, prod_sales[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='red')

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Show the plot
plt.show()