import matplotlib.pyplot as plt
import numpy as np

departments = ['Software Dev', 'Product Management', 'Marketing', 'Sales']
software_dev_hours = [40, 42, 43, 45, 45, 44, 46, 47, 42, 43, 41, 40, 45, 46]
product_mgmt_hours = [38, 39, 41, 35, 36, 37, 39, 40, 41, 38, 37, 36, 38, 39]
marketing_hours = [35, 36, 37, 32, 34, 35, 36, 37, 33, 34, 35, 36, 37, 36]
sales_hours = [43, 45, 44, 42, 43, 44, 45, 46, 47, 46, 45, 44, 43, 45]

working_hours_data = [software_dev_hours, product_mgmt_hours, marketing_hours, sales_hours]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 7))

box1 = ax1.boxplot(working_hours_data, vert=False, patch_artist=True, labels=departments, notch=True, widths=0.7)
colors = ['lightblue', 'peachpuff', 'lightgreen', 'lightsalmon']
for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)
for median in box1['medians']:
    median.set(color='firebrick', linewidth=2)

ax1.set_xlabel('Hours per Week')

num_employees = [50, 30, 20, 40]

ax2.bar(departments, num_employees, color=colors)
ax2.set_xlabel('Departments')
ax2.set_ylabel('Number of Employees')

for bar, height in zip(ax2.patches, num_employees):
    ax2.text(bar.get_x() + bar.get_width() / 2, height - 3, str(int(height)), ha='center', va='bottom', color='black')

plt.tight_layout()
plt.show()