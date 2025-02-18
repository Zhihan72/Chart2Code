import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])
average_sales = np.array([5, 7, 8, 10, 12, 9, 13, 15, 14, 16, 14, 13])

plt.figure(figsize=(14, 8))

# Plotting two series
width = 0.35
x_indices = np.arange(len(months))

plt.bar(x_indices - width/2, average_users, width, label='Average Users', color='darkorange', alpha=0.8)
plt.bar(x_indices + width/2, average_sales, width, label='Average Sales (hundreds)', color='steelblue', alpha=0.8)

plt.ylim(0, 55)
plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Average Users and Sales per Month')
plt.xticks(x_indices, months)
plt.legend()

plt.tight_layout()
plt.show()