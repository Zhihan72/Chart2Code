import matplotlib.pyplot as plt
import numpy as np

# Define months and performance data for each department
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Performance data (scores out of 100) for each department over the year
sales_performance = np.array([85, 88, 90, 93, 95, 85, 92, 94, 96, 91, 89, 90])
rnd_performance = np.array([78, 80, 82, 81, 85, 83, 86, 89, 88, 90, 87, 86])
cust_support_performance = np.array([70, 73, 75, 78, 79, 77, 80, 82, 81, 83, 85, 84])

# Variability (error) data for each department
sales_error = np.array([3, 2, 4, 1, 2, 3, 2, 3, 2, 1, 2, 3])
rnd_error = np.array([2, 3, 1, 2, 3, 2, 3, 2, 1, 2, 4, 3])
cust_support_error = np.array([5, 3, 4, 2, 3, 2, 4, 2, 3, 2, 1, 2])

# Setup the plot figure
plt.figure(figsize=(14, 8))

# Plot performance trends for each department with error bars
plt.errorbar(months, sales_performance, yerr=sales_error, fmt='-o',
             color='navy', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
plt.errorbar(months, rnd_performance, yerr=rnd_error, fmt='-s',
             color='crimson', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)
plt.errorbar(months, cust_support_performance, yerr=cust_support_error, fmt='-^',
             color='forestgreen', linestyle='-', linewidth=2, capsize=5, elinewidth=1.5, alpha=0.8)

# Add titles and labels
plt.title("Monthly Performance Trends of Company Departments\nYear 2023 Analysis", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Performance Score (out of 100)", fontsize=14)

# Remove the legend, grid, and borders
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()