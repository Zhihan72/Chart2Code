import matplotlib.pyplot as plt
import numpy as np

# Original data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])

# Sort data by average_users in ascending order
sorted_indices = np.argsort(average_users)
sorted_months = months[sorted_indices]
sorted_users = average_users[sorted_indices]

plt.figure(figsize=(14, 8))
plt.bar(sorted_months, sorted_users, color='darkorange', alpha=0.8)

plt.ylim(15, 55)
plt.xlabel('Months')
plt.ylabel('Average Users')
plt.title('Average Users per Month (Sorted)')

plt.tight_layout()
plt.show()