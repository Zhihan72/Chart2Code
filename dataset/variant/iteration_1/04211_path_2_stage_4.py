import matplotlib.pyplot as plt
import numpy as np

# Shuffled fruit types
fruit_types = ['Cherry', 'Banana', 'Elderberry', 'Apple', 'Date']

# Manually shuffled content within each fruit's data
usage_data = np.array([
    [60, 35, 40, 45, 30],  # Elderberry
    [65, 50, 60, 55, 80],  # Cherry
    [190, 150, 180, 170, 160],  # Apple
    [70, 40, 50, 55, 45],  # Date
    [160, 150, 135, 140, 155]   # Banana
])

# Compute total usage across all fruits
total_usage = usage_data.sum(axis=1)

# Sort the fruit types by total usage
sorted_indices = np.argsort(total_usage)

sorted_fruit_types = [fruit_types[i] for i in sorted_indices]
sorted_total_usage = total_usage[sorted_indices]

fig, ax = plt.subplots(figsize=(10, 6))

# Use a single color for all bars
color = '#3498db'

# Plot sorted bar chart
ax.bar(sorted_fruit_types, sorted_total_usage, color=color)

# Randomly altered chart labels
ax.set_xlabel('Types of Fruits', fontsize=12)
ax.set_ylabel('Instances of Total Usage', fontsize=12)
ax.set_title('Usage of Fruits Over Five Years', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()