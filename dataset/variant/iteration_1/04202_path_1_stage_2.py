import matplotlib.pyplot as plt
import numpy as np

departments = ['Dev Team', 'Prod Mgmt', 'Ad Team', 'Sales Force']

software_dev_hours = [40, 42, 43, 45, 45, 44, 46, 47, 42, 43, 41, 40, 45, 46]
product_mgmt_hours = [38, 39, 41, 35, 36, 37, 39, 40, 41, 38, 37, 36, 38, 39]
marketing_hours = [35, 36, 37, 32, 34, 35, 36, 37, 33, 34, 35, 36, 37, 36]
sales_hours = [43, 45, 44, 42, 43, 44, 45, 46, 47, 46, 45, 44, 43, 45]

working_hours_data = [software_dev_hours, product_mgmt_hours, marketing_hours, sales_hours]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 7))
fig.suptitle('Company Division Insights', fontsize=16, fontweight='bold', y=1.02)

box1 = ax1.boxplot(working_hours_data, vert=False, patch_artist=True, labels=departments, notch=False, widths=0.5)
colors = ['cornflowerblue', 'bisque', 'palegreen', 'salmon']
for patch, color in zip(box1['boxes'], colors):
    patch.set_facecolor(color)
for cap in box1['caps']:
    cap.set(color='black', linewidth=1)
for median in box1['medians']:
    median.set(color='limegreen', linewidth=1.5)

ax1.set_title('Weekly Hours by Team', fontsize=14)
ax1.set_xlabel('Hours/Week', fontsize=12)
ax1.xaxis.grid(True, color='silver', linestyle='-', alpha=0.5)

num_employees = [50, 30, 20, 40]

bars = ax2.bar(departments, num_employees, color=colors, hatch='//')
ax2.set_title('Team Size Comparison', fontsize=14)
ax2.set_xlabel('Teams', fontsize=12)
ax2.set_ylabel('Employees Count', fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, height - 3, '%d' % int(height), ha='center', va='bottom', color='darkred', fontsize=10)

plt.tight_layout()
plt.show()