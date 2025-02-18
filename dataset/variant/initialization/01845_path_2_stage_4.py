import matplotlib.pyplot as plt
import numpy as np

years = np.array(list(range(2015, 2026)))

# Sample data
python_popularity = [20, 25, 30, 35, 42, 48, 55, 60, 66, 70, 75]
javascript_popularity = [30, 28, 27, 25, 23, 22, 20, 19, 18, 17, 15]
java_popularity = [25, 24, 23, 22, 20, 18, 17, 15, 13, 12, 10]

plt.figure(figsize=(12, 6))

# Use different colors and styles for each line
plt.plot(years, python_popularity, marker='D', linestyle='-.', color='green', linewidth=2, label='Python')
plt.plot(years, javascript_popularity, marker='<', linestyle='-', color='blue', linewidth=2, label='JavaScript')
plt.plot(years, java_popularity, marker='>', linestyle='--', color='orange', linewidth=2, label='Java')

# Altered legends
plt.legend(loc='upper left')

# Customizing grids and removing borders
plt.grid(True, linestyle='-', alpha=0.7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.xticks(years, rotation=45)
plt.yticks(range(0, 81, 10))

plt.tight_layout()
plt.show()