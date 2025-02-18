import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])

sorted_indices = np.argsort(average_users)
months_sorted = months[sorted_indices]
average_users_sorted = average_users[sorted_indices]

plt.figure(figsize=(14, 8))

plt.bar(months_sorted, average_users_sorted, color='teal', alpha=0.75, edgecolor='black', linestyle='-.')

plt.title('Monthly Active Users Sorted by Activity', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Monthly Active Users (in thousands)', fontsize=12)

plt.ylim(15, 55)
plt.xticks(fontsize=10)
plt.yticks(np.arange(15, 60, 5), fontsize=10)

plt.grid(True, linestyle=':', linewidth=0.9, alpha=0.8)

plt.tight_layout()

plt.show()