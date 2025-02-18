import matplotlib.pyplot as plt
import numpy as np

# Months of the year
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Average monthly active users (in thousands) over a year
average_users = np.array([20, 23, 25, 28, 35, 30, 40, 50, 48, 45, 42, 38])

# Sort the data in descending order
sorted_indices = np.argsort(average_users)
months_sorted = months[sorted_indices]
average_users_sorted = average_users[sorted_indices]

# Setting up the plot
plt.figure(figsize=(14, 8))

# Plotting the sorted bar chart
plt.bar(months_sorted, average_users_sorted, color='darkorange', alpha=0.8)

# Titles and labels
plt.title('Monthly Active Users Sorted by Activity', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Monthly Active Users (in thousands)', fontsize=12)

# Customize axes for improved visibility
plt.ylim(15, 55)
plt.xticks(fontsize=10)
plt.yticks(np.arange(15, 60, 5), fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()