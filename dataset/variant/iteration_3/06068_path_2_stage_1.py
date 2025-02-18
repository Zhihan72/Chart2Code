import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
departments = ['Development', 'Marketing', 'Sales']

# Altered productivity data while keeping the structure intact
prod_development = [15, 20, 10, 18, 28, 16, 22, 30, 17, 27, 35, 24]
prod_marketing = [16, 12, 22, 14, 21, 15, 25, 26, 19, 20, 30, 28]
prod_sales = [18, 22, 19, 25, 30, 20, 27, 33, 29, 26, 34, 29]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, prod_development, marker='o', linestyle='-', color='blue', label='Development Dept.')
ax.plot(months, prod_marketing, marker='s', linestyle='--', color='green', label='Marketing Dept.')
ax.plot(months, prod_sales, marker='^', linestyle=':', color='red', label='Sales Dept.')

ax.set_title('Monthly Productivity Trends in a Tech Company (2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Productivity Units', fontsize=12)
ax.set_xlabel('Months', fontsize=12)
ax.legend(title='Departments', fontsize=12, loc='upper left')

ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

for i, month in enumerate(months):
    ax.annotate(f"{prod_development[i]} u", (month, prod_development[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='blue')
    ax.annotate(f"{prod_marketing[i]} u", (month, prod_marketing[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='green')
    ax.annotate(f"{prod_sales[i]} u", (month, prod_sales[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, color='red')

plt.tight_layout()
plt.show()