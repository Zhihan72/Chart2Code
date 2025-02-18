import matplotlib.pyplot as plt
import numpy as np

years = np.array(list(range(2015, 2026)))
python_popularity = [20, 25, 30, 35, 42, 48, 55, 60, 66, 70, 75]
javascript_popularity = [30, 28, 27, 25, 23, 22, 20, 19, 18, 17, 15]
java_popularity = [25, 24, 23, 22, 20, 18, 17, 15, 13, 12, 10]
cpp_popularity = [25, 23, 20, 18, 15, 12, 8, 6, 3, 1, 0]

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