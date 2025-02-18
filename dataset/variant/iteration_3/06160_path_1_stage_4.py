import matplotlib.pyplot as plt
import numpy as np

# Preserving the original dimensional structure, but altering the data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temps_2021 = np.array([5, 3, 14, 8, 18, 22, 25, 20, 4, 14, 9, 24])  # Altered values
temps_2022 = np.array([8, 4, 19, 7, 17, 21, 24, 13, 3, 13, 2, 23])  # Altered values
temps_2023 = np.array([12, 1, 18, 6, 16, 20, 23, 12, 2, 12, 7, 22]) # Altered values

fig, ax = plt.subplots(figsize=(12, 6))

# Plot each year's data with the same color
ax.plot(months, temps_2021, marker='v', linestyle=':', color='b', linewidth=2)
ax.plot(months, temps_2022, marker='x', linestyle='-.', color='b', linewidth=2)
ax.plot(months, temps_2023, marker='p', linestyle='-', color='b', linewidth=2)

plt.xticks(rotation=45)
ax.grid(alpha=0.5, linestyle='-', linewidth=1)

plt.tight_layout()
plt.show()