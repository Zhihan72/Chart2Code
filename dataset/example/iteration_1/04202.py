import matplotlib.pyplot as plt
import numpy as np

# Define the departments in a tech company
departments = ['Software Dev', 'Product Management', 'Marketing', 'Sales']

# Create artificial data representing the working hours per week for each department
software_dev_hours = [40, 42, 43, 45, 45, 44, 46, 47, 42, 43, 41, 40, 45, 46]
product_mgmt_hours = [38, 39, 41, 35, 36, 37, 39, 40, 41, 38, 37, 36, 38, 39]
marketing_hours = [35, 36, 37, 32, 34, 35, 36, 37, 33, 34, 35, 36, 37, 36]
sales_hours = [43, 45, 44, 42, 43, 44, 45, 46, 47, 46, 45, 44, 43, 45]

# Combine the data
working_hours_data = [software_dev_hours, product_mgmt_hours, marketing_hours, sales_hours]

# Create a figure with a title and two subplots
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 7))
fig.suptitle('Work-Life Balance in a Tech Company', fontsize=16, fontweight='bold', y=1.02)

# Plot horizontal box plots showing working hours for each department
box1 = ax1.boxplot(working_hours_data, vert=False, patch_artist=True, labels=departments, notch=True, widths=0.7)
colors = ['lightblue', 'peachpuff', 'lightgreen', 'lightsalmon']
for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)
for cap in box1['caps']:
    cap.set(color='grey', linewidth=1.2)
for median in box1['medians']:
    median.set(color='firebrick', linewidth=2)

ax1.set_title('Weekly Working Hours by Department', fontsize=14)
ax1.set_xlabel('Hours per Week', fontsize=12)
ax1.xaxis.grid(True, color='grey', linestyle='--', alpha=0.7)

# Create artificial data for the number of employees in each department
num_employees = [50, 30, 20, 40]

# Plot bar chart showing the number of employees in each department
bars = ax2.bar(departments, num_employees, color=colors)
ax2.set_title('Number of Employees by Department', fontsize=14)
ax2.set_xlabel('Departments', fontsize=12)
ax2.set_ylabel('Number of Employees', fontsize=12)

# Add value labels on the bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, height - 3, '%d' % int(height), ha='center', va='bottom', color='black', fontsize=10)

# Optimize layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()