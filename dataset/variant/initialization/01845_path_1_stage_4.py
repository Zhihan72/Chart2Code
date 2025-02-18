import matplotlib.pyplot as plt
import numpy as np

years = np.array(list(range(2015, 2026)))

# Randomly altered popularity data within each language group while maintaining the original length
python_popularity = [48, 30, 42, 60, 70, 20, 55, 75, 25, 66, 35]
javascript_popularity = [22, 17, 23, 18, 19, 27, 30, 28, 25, 15, 20]
java_popularity = [18, 23, 13, 15, 12, 24, 25, 10, 20, 22, 17]
cpp_popularity = [12, 18, 25, 3, 1, 0, 6, 15, 20, 23, 8]

plt.figure(figsize=(12, 6))
consistent_color = 'blue'
plt.plot(years, python_popularity, marker='o', linestyle='-', color=consistent_color, linewidth=2)
plt.plot(years, javascript_popularity, marker='s', linestyle='--', color=consistent_color, linewidth=2)
plt.plot(years, java_popularity, marker='^', linestyle='-.', color=consistent_color, linewidth=2)
plt.plot(years, cpp_popularity, marker='x', linestyle=':', color=consistent_color, linewidth=2)

plt.xticks(years, rotation=45)
plt.yticks(range(0, 81, 10))

plt.tight_layout()
plt.show()