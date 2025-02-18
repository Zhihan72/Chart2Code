import matplotlib.pyplot as plt
import numpy as np

# Fruit types and their total usage over the years
fruit_types = ['Apple', 'Cherry', 'Date', 'Elderberry']
total_usage = np.sum(np.array([
    [150, 160, 170, 180, 190],  # Apple
    [50, 55, 60, 65, 80],       # Cherry
    [40, 45, 50, 55, 70],       # Date
    [30, 35, 40, 45, 60]        # Elderberry
]), axis=1)

# Sort fruits by total usage in descending order
sorted_indices = np.argsort(total_usage)[::-1]
sorted_fruits = np.array(fruit_types)[sorted_indices]
sorted_usage = total_usage[sorted_indices]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_fruits, sorted_usage, color=['#e74c3c', '#8e44ad', '#16a085', '#3498db'])

# Set labels and title
plt.xlabel('Fruit Type', fontsize=12)
plt.ylabel('Total Usage Instances', fontsize=12)
plt.title('Total Fruit Usage in Consumer Products (2018-2022)', fontsize=16, fontweight='bold', pad=20)

# Display the sorted bar chart
plt.tight_layout()
plt.show()