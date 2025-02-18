import matplotlib.pyplot as plt
import numpy as np

fruit_types = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# Manually shuffled content within each fruit's data
usage_data = np.array([
    [190, 150, 180, 170, 160],  # Apple
    [160, 150, 135, 140, 155],  # Banana
    [65, 50, 60, 55, 80],       # Cherry
    [70, 40, 50, 55, 45],       # Date
    [60, 35, 40, 45, 30]        # Elderberry
])

# Compute total usage across all years
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

ax.set_xlabel('Fruit Type', fontsize=12)
ax.set_ylabel('Total Usage Instances', fontsize=12)
ax.set_title('Total Fruit Usage Sorted Over 5 Years', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()