import matplotlib.pyplot as plt
import numpy as np

# Original data
hours_of_coding = np.array([5, 6, 8, 7, 9, 4, 3])
caffeine_consumption = np.array([2, 3, 4, 3, 5, 2, 1])
tiredness_level = np.array([4, 5, 7, 6, 8, 3, 2])
marker_sizes_coding = tiredness_level * 20

# New data for another group
hours_of_exercise = np.array([1, 2, 1, 3, 2, 1, 2])
performance_level = np.array([7, 6, 6, 8, 7, 5, 6])
marker_sizes_exercise = performance_level * 20

# Colors for two different data series
colors_coding = np.array([
    [0.267004, 0.004874, 0.329415, 1.],
    [0.127568, 0.566949, 0.550556, 1.],
    [0.993248, 0.906157, 0.143936, 1.],
    [0.253935, 0.265254, 0.529983, 1.],
    [0.369214, 0.788888, 0.382914, 1.],
    [0.993248, 0.906157, 0.143936, 1.],
    [0.127568, 0.566949, 0.550556, 1.]
])

colors_exercise = np.array([
    [0.604776, 0.278756, 0.631071, 1.],
    [0.901065, 0.561559, 0.331776, 1.],
    [0.267004, 0.004874, 0.329415, 1.],
    [0.335488, 0.803445, 0.375224, 1.],
    [0.240846, 0.602513, 0.808753, 1.],
    [0.993248, 0.906157, 0.143936, 1.],
    [0.800987, 0.378190, 0.696820, 1.]
])

plt.figure(figsize=(12, 7))

# Plot original coding data
plt.scatter(hours_of_coding, caffeine_consumption, s=marker_sizes_coding, c=colors_coding, alpha=0.8, edgecolors='black', linewidth=1, label='Coding vs Caffeine')

# Plot new exercise data
plt.scatter(hours_of_exercise, performance_level, s=marker_sizes_exercise, c=colors_exercise, alpha=0.8, edgecolors='black', linewidth=1, label='Exercise vs Performance')

plt.legend()
plt.xlabel('Hours')
plt.ylabel('Level')
plt.title('Coding and Exercise Data Comparison')
plt.tight_layout()
plt.show()