import matplotlib.pyplot as plt
import numpy as np

departments = ['Software Development', 'Marketing', 'Sales', 'Human Resources', 'Customer Support']
days = np.arange(1, 8)

software_dev = np.array([80, 85, 83, 90, 88, 85, 84])
marketing = np.array([60, 62, 61, 65, 66, 62, 60])
sales = np.array([50, 55, 53, 58, 56, 54, 55])
hr = np.array([30, 32, 31, 34, 33, 32, 30])
customer_support = np.array([70, 72, 75, 77, 76, 74, 73])

data = np.vstack([software_dev, marketing, sales, hr, customer_support])

fig, axs = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Departmental Productivity Trends Over a Week\nat Tech World Inc.', fontsize=18, fontweight='bold')

# Line Plot for Total Productivity (now at the top)
total_productivity = data.sum(axis=0)
axs[0].plot(days, total_productivity, label='Total Productivity', color='#ff6f61', linestyle='-', marker='o', linewidth=2)
axs[0].fill_between(days, 0, total_productivity, color='#ff9e9d', alpha=0.5)
axs[0].set_title('Total Productivity Over the Week', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Day of the Week', fontsize=12)
axs[0].set_ylabel('Total Productivity Units', fontsize=12)
axs[0].set_xticks(days)
axs[0].set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
axs[0].grid(True, linestyle='--', linewidth=0.5)
axs[0].legend(loc='upper left', fontsize=10)

# Stacked Area Chart (now at the bottom)
axs[1].stackplot(days, data, labels=departments, 
                 colors=['#4e79a7', '#f28e2b', '#76b7b2', '#59a14f', '#edc948'], alpha=0.8)
axs[1].set_title('Daily Productivity by Department', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Day of the Week', fontsize=12)
axs[1].set_ylabel('Productivity Units', fontsize=12)
axs[1].set_xticks(days)
axs[1].set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
axs[1].legend(loc='upper right', fontsize=10, title='Departments')
axs[1].grid(True, linestyle='--', linewidth=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()