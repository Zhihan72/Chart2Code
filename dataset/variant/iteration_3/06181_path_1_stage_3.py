import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

max_temp_2022 = np.array([5, 6, 15, 16, 21, 30, 25, 29, 24, 10, 11, 6])
min_temp_2022 = np.array([-3, -1, 3, 6, 9, 14, 17, 18, 12, 4, 3, -2])
max_temp_2023 = np.array([7, 9, 13, 20, 19, 25, 31, 28, 27, 18, 12, 8])
min_temp_2023 = np.array([-1, 0, 4, 7, 10, 15, 20, 19, 14, 9, 5, 1])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, max_temp_2022, color='green', marker='x', linestyle=':', linewidth=2)
ax.plot(months, min_temp_2022, color='purple', marker='+', linestyle='-.', linewidth=2)
ax.plot(months, max_temp_2023, color='black', marker='*', linestyle='-', linewidth=2)
ax.plot(months, min_temp_2023, color='brown', marker='^', linestyle='--', linewidth=2)

ax.grid(visible=False)

ax.legend(["Max Temp 2022", "Min Temp 2022", "Max Temp 2023", "Min Temp 2023"], loc='upper left', frameon=False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()