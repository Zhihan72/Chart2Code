import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

max_temp_2022 = np.array([5, 6, 15, 16, 21, 30, 25, 29, 24, 10, 11, 6])
min_temp_2022 = np.array([-3, -1, 3, 6, 9, 14, 17, 18, 12, 4, 3, -2])
max_temp_2023 = np.array([7, 9, 13, 20, 19, 25, 31, 28, 27, 18, 12, 8])
min_temp_2023 = np.array([-1, 0, 4, 7, 10, 15, 20, 19, 14, 9, 5, 1])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, max_temp_2022, color='red', marker='o', linestyle='-', linewidth=2)
ax.plot(months, min_temp_2022, color='blue', marker='o', linestyle='-', linewidth=2)
ax.plot(months, max_temp_2023, color='orange', marker='s', linestyle='--', linewidth=2)
ax.plot(months, min_temp_2023, color='cyan', marker='s', linestyle='--', linewidth=2)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()