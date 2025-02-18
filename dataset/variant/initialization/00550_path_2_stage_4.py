import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])

plt.figure(figsize=(14, 8))
plt.bar(months, average_users, color='darkorange', alpha=0.8)

plt.ylim(15, 55)
plt.xlabel('Months')
plt.ylabel('Average Users')
plt.title('Average Users per Month')

plt.tight_layout()
plt.show()