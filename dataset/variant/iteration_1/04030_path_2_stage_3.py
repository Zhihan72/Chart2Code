import matplotlib.pyplot as plt
import numpy as np

hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])
marker_sizes = tiredness_level * 20

# Shuffled colors manually
colors = np.array([
    [0.267004, 0.004874, 0.329415, 1.],  # Previously color for point 1, now assigned to point 3
    [0.127568, 0.566949, 0.550556, 1.],  # Previously color for point 4, now assigned to point 5
    [0.993248, 0.906157, 0.143936, 1.],  # Previously color for point 7, now assigned to point 6
    [0.253935, 0.265254, 0.529983, 1.],  # Previously color for point 3, now assigned to point 1
    [0.369214, 0.788888, 0.382914, 1.],  # Previously color for point 6, now assigned to point 2
    [0.993248, 0.906157, 0.143936, 1.],  # Previously color for point 2, now assigned to point 4
    [0.127568, 0.566949, 0.550556, 1.]   # Previously color for point 5, now assigned to point 7
])

plt.figure(figsize=(12, 7))
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes, c=colors, alpha=0.8, edgecolors='black', linewidth=1, cmap='viridis')

plt.tight_layout()
plt.show()