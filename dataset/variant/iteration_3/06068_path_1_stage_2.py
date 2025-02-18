import matplotlib.pyplot as plt
import numpy as np

# Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
departments = ['Development', 'Marketing', 'Sales', 'Customer Support']

# Productivity data
prod_development = [i * 1.5 for i in [10, 13, 8, 15, 20, 18, 25, 22, 19, 25, 30, 28]]
prod_marketing = [i * 1.4 for i in [12, 10, 15, 11, 18, 17, 19, 25, 23, 21, 26, 24]]
prod_sales = [i * 1.6 for i in [14, 18, 16, 20, 24, 22, 26, 30, 28, 27, 32, 30]]
prod_customer_support = [i * 1.2 for i in [11, 14, 12, 17, 21, 19, 23, 28, 26, 24, 27, 29]]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data for each department
ax.plot(months, prod_development, marker='o', linestyle='-', color='blue', label='Dept. Dev')
ax.plot(months, prod_marketing, marker='s', linestyle='--', color='green', label='Dept. Mark')
ax.plot(months, prod_sales, marker='^', linestyle=':', color='red', label='Dept. Sales')
ax.plot(months, prod_customer_support, marker='D', linestyle='-.', color='purple', label='Dept. Support')

# Set titles and labels
ax.set_title('Yearly Output Patterns at a Tech Firm (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Unit Count of Productivity', fontsize=12)
ax.set_xlabel('Timeframe: Months', fontsize=12)
ax.legend(title='Sector Groups', fontsize=12, loc='upper left')

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate specific data points
for i, month in enumerate(months):
    ax.annotate(f"{prod_development[i]} units", (month, prod_development[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='blue')
    ax.annotate(f"{prod_marketing[i]} units", (month, prod_marketing[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='green')
    ax.annotate(f"{prod_sales[i]} units", (month, prod_sales[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='red')
    ax.annotate(f"{prod_customer_support[i]} units", (month, prod_customer_support[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='purple')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()