import matplotlib.pyplot as plt
import numpy as np

# User data representing monthly active users (in thousands)
months = np.array(['Dec', 'Aug', 'Jan', 'Apr', 'Jun', 'May', 'Feb', 'Sep', 'Jul', 'Nov', 'Oct', 'Mar'])
average_users = np.array([40, 35, 28, 45, 25, 38, 20, 48, 23, 50, 42, 30])

plt.figure(figsize=(14, 8))

plt.bar(months, average_users, color='teal', edgecolor='black', linestyle='-.')

plt.title('User Statistics: Varied Engagement Across Months', fontsize=16, fontweight='bold')
plt.xlabel('Timeframe', fontsize=12)
plt.ylabel('Active Users (000s)', fontsize=12)

plt.ylim(15, 55)
plt.xticks(fontsize=10)
plt.yticks(np.arange(15, 60, 5), fontsize=10)

plt.grid(True, linestyle=':', linewidth=0.9, alpha=0.8)

plt.tight_layout()

plt.show()