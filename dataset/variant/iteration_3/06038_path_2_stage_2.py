import matplotlib.pyplot as plt
import numpy as np

# Define performance data for each department
departments = np.array(['Sales', 'R&D', 'Customer Support'])

# Aggregate performance scores by department
sales_total = np.mean([85, 88, 90, 93, 95, 85, 92, 94, 96, 91, 89, 90])
rnd_total = np.mean([78, 80, 82, 81, 85, 83, 86, 89, 88, 90, 87, 86])
cust_support_total = np.mean([70, 73, 75, 78, 79, 77, 80, 82, 81, 83, 85, 84])

# Average performance scores for each department
performance_scores = np.array([sales_total, rnd_total, cust_support_total])

# Aggregate error data by department
sales_avg_error = np.mean([3, 2, 4, 1, 2, 3, 2, 3, 2, 1, 2, 3])
rnd_avg_error = np.mean([2, 3, 1, 2, 3, 2, 3, 2, 1, 2, 4, 3])
cust_support_avg_error = np.mean([5, 3, 4, 2, 3, 2, 4, 2, 3, 2, 1, 2])

# Average error for each department
performance_errors = np.array([sales_avg_error, rnd_avg_error, cust_support_avg_error])

# Plot figure setup
plt.figure(figsize=(10, 6))

# Create horizontal bar chart
plt.barh(departments, performance_scores, xerr=performance_errors, 
         color=['navy', 'crimson', 'forestgreen'], edgecolor='gray', alpha=0.8, capsize=5)

# Add titles and labels
plt.title("Average Performance Scores of Company Departments\nYear 2023 Analysis", fontsize=18, pad=20)
plt.xlabel("Average Performance Score (out of 100)", fontsize=14)
plt.ylabel("Department", fontsize=14)

# Display chart
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()