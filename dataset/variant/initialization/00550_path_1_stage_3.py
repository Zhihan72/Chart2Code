import matplotlib.pyplot as plt
import numpy as np

# Randomly shuffled user data while keeping the monthly structure intact
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
average_users = np.array([40, 35, 28, 45, 25, 38, 20, 48, 23, 50, 42, 30])

plt.figure(figsize=(14, 8))

# The content within certain data groups (average_users) is shuffled, months remain the same
plt.bar(months, average_users, color='teal', alpha=0.75, edgecolor='black', linestyle='-.')

plt.title('Monthly Active Users with Randomized User Activity', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Monthly Active Users (in thousands)', fontsize=12)

plt.ylim(15, 55)
plt.xticks(fontsize=10)
plt.yticks(np.arange(15, 60, 5), fontsize=10)

plt.grid(True, linestyle=':', linewidth=0.9, alpha=0.8)

plt.tight_layout()

plt.show()