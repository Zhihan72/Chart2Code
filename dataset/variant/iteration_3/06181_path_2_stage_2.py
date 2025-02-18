import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

max_temp_2022 = np.array([5, 7, 12, 16, 21, 25, 29, 28, 24, 18, 11, 6])
min_temp_2022 = np.array([-3, -2, 1, 6, 10, 14, 18, 17, 12, 8, 3, -1])
max_temp_2023 = np.array([6, 8, 13, 17, 22, 26, 30, 29, 25, 19, 12, 7])
min_temp_2023 = np.array([-2, -1, 2, 7, 11, 15, 19, 18, 13, 9, 4, 0])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, max_temp_2022, color='purple', marker='o', linestyle='-', linewidth=2)
ax.plot(months, min_temp_2022, color='green', marker='o', linestyle='-', linewidth=2)
ax.plot(months, max_temp_2023, color='brown', marker='s', linestyle='--', linewidth=2)
ax.plot(months, min_temp_2023, color='pink', marker='s', linestyle='--', linewidth=2)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()