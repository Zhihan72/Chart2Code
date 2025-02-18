import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
sales_performance = np.array([85, 88, 90, 93, 95, 85, 92, 94, 96, 91, 89, 90])
rnd_performance = np.array([78, 80, 82, 81, 85, 83, 86, 89, 88, 90, 87, 86])
cust_support_performance = np.array([70, 73, 75, 78, 79, 77, 80, 82, 81, 83, 85, 84])
marketing_performance = np.array([65, 68, 70, 72, 74, 73, 75, 77, 79, 78, 76, 77])
finance_performance = np.array([88, 85, 87, 90, 89, 91, 90, 92, 94, 93, 92, 91])

sales_error = np.array([3, 2, 4, 1, 2, 3, 2, 3, 2, 1, 2, 3])
rnd_error = np.array([2, 3, 1, 2, 3, 2, 3, 2, 1, 2, 4, 3])
cust_support_error = np.array([5, 3, 4, 2, 3, 2, 4, 2, 3, 2, 1, 2])
marketing_error = np.array([4, 3, 3, 2, 2, 3, 3, 2, 1, 2, 3, 4])
finance_error = np.array([2, 3, 2, 1, 2, 1, 3, 2, 3, 2, 3, 2])

plt.figure(figsize=(14, 10))

plt.errorbar(months, sales_performance, yerr=sales_error, fmt='--d',
             color='darkorange', linestyle='--', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)
plt.errorbar(months, rnd_performance, yerr=rnd_error, fmt=':p',
             color='mediumseagreen', linestyle=':', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)
plt.errorbar(months, cust_support_performance, yerr=cust_support_error, fmt='-.h',
             color='crimson', linestyle='-.', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)
plt.errorbar(months, marketing_performance, yerr=marketing_error, fmt='-o',
             color='royalblue', linestyle='-', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)
plt.errorbar(months, finance_performance, yerr=finance_error, fmt='-s',
             color='purple', linestyle='-', linewidth=2, capsize=4, elinewidth=1.0, alpha=0.9)

plt.grid(True, linestyle=':', linewidth=0.6, alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()