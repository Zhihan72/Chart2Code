import matplotlib.pyplot as plt
import numpy as np

fruit_types = ['Apple', 'Cherry', 'Date', 'Elderberry']
total_usage = np.sum(np.array([
    [150, 160, 170, 180, 190],  # Apple
    [50, 55, 60, 65, 80],       # Cherry
    [40, 45, 50, 55, 70],       # Date
    [30, 35, 40, 45, 60]        # Elderberry
]), axis=1)

sorted_indices = np.argsort(total_usage)[::-1]
sorted_fruits = np.array(fruit_types)[sorted_indices]
sorted_usage = total_usage[sorted_indices]

plt.figure(figsize=(10, 6))
plt.bar(sorted_fruits, sorted_usage, color=['#e74c3c', '#8e44ad', '#16a085', '#3498db'])

plt.xticks([])
plt.yticks([])

plt.show()