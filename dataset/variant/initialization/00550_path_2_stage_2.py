import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])
user_variability = np.array([2, 1.5, 3, 2.5, 4, 3, 5, 4, 3.5, 2.5, 4, 2])

plt.figure(figsize=(14, 8))
plt.errorbar(months, average_users, yerr=user_variability, fmt='-o', color='darkorange', capsize=5, alpha=0.8, elinewidth=2, markerfacecolor='white')

plt.ylim(15, 55)

plt.tight_layout()
plt.show()