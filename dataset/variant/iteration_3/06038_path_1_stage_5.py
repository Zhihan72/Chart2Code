import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Performance data for each department
performances = {
    'Sales': np.array([85, 88, 90, 93, 95, 85, 92, 94, 96, 91, 89, 90]),
    'R&D': np.array([78, 80, 82, 81, 85, 83, 86, 89, 88, 90, 87, 86]),
    'Customer Support': np.array([70, 73, 75, 78, 79, 77, 80, 82, 81, 83, 85, 84]),
    'Marketing': np.array([65, 68, 70, 72, 74, 73, 75, 77, 79, 78, 76, 77]),
    'Finance': np.array([88, 85, 87, 90, 89, 91, 90, 92, 94, 93, 92, 91])
}

# Sorting the data
for dept in performances:
    performances[dept] = np.sort(performances[dept])

# Number of departments
n_depts = len(performances)
width = 0.15  # width of the bars

# Plot each department's performance
plt.figure(figsize=(14, 10))
index = np.arange(len(months))

for i, (dept_name, performance_data) in enumerate(performances.items()):
    plt.bar(index + i * width, performance_data, width, label=dept_name)

# Customize the plot
plt.xlabel('Months')
plt.ylabel('Performance')
plt.title('Performance by department across months')
plt.xticks(index + width * (n_depts - 1) / 2, months, fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()