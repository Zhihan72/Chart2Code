import matplotlib.pyplot as plt
import numpy as np

fruit_types = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

usage_data = np.array([
    [150, 160, 170, 180, 190],  # Apple
    [140, 135, 150, 160, 155],  # Banana
    [50, 55, 60, 65, 80],       # Cherry
    [40, 45, 50, 55, 70],       # Date
    [30, 35, 40, 45, 60]        # Elderberry
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