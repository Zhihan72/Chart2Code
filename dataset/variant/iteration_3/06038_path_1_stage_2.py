import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
sales_performance = np.array([85, 88, 90, 93, 95, 85, 92, 94, 96, 91, 89, 90])
rnd_performance = np.array([78, 80, 82, 81, 85, 83, 86, 89, 88, 90, 87, 86])
cust_support_performance = np.array([70, 73, 75, 78, 79, 77, 80, 82, 81, 83, 85, 84])

sales_error = np.array([3, 2, 4, 1, 2, 3, 2, 3, 2, 1, 2, 3])
rnd_error = np.array([2, 3, 1, 2, 3, 2, 3, 2, 1, 2, 4, 3])
cust_support_error = np.array([5, 3, 4, 2, 3, 2, 4, 2, 3, 2, 1, 2])

plt.figure(figsize=(14, 8))

plt.errorbar(months, sales_performance, yerr=sales_error, fmt='--d', label='Sales',
             color='darkorange', linestyle='--', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)
plt.errorbar(months, rnd_performance, yerr=rnd_error, fmt=':p', label='R&D',
             color='mediumseagreen', linestyle=':', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)
plt.errorbar(months, cust_support_performance, yerr=cust_support_error, fmt='-.h', label='Customer Support',
             color='crimson', linestyle='-.', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)

plt.title("Monthly Performance Trends of Company Departments\nYear 2023 Analysis", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Performance Score (out of 100)", fontsize=14)
plt.legend(loc='lower right', title='Departments', fontsize=12, title_fontsize='13')
plt.grid(True, linestyle=':', linewidth=0.6, alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()