import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temps_2021 = np.array([3, 5, 9, 14, 18, 22, 25, 24, 20, 14, 8, 4])
temps_2022 = np.array([2, 4, 8, 13, 17, 21, 24, 23, 19, 13, 7, 3])
temps_2023 = np.array([1, 3, 7, 12, 16, 20, 23, 22, 18, 12, 6, 2])

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each year's data with the same color
ax.plot(months, temps_2021, marker='v', linestyle=':', color='b', linewidth=2)
ax.plot(months, temps_2022, marker='x', linestyle='-.', color='b', linewidth=2)
ax.plot(months, temps_2023, marker='p', linestyle='-', color='b', linewidth=2)

plt.xticks(rotation=45)
ax.grid(alpha=0.5, linestyle='-', linewidth=1)

plt.tight_layout()
plt.show()