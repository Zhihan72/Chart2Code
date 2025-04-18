import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
la_temps = np.array([14, 15, 17, 19, 22, 24, 27, 27, 26, 22, 18, 15])
ny_temps = np.array([0, 1, 7, 13, 19, 24, 27, 26, 22, 15, 10, 4])
chicago_temps = np.array([-3, 0, 6, 12, 18, 23, 26, 25, 20, 13, 6, -1])

fig, ax = plt.subplots(figsize=(12, 8))

# Use a single color for all cities
single_color = 'purple'
ax.plot(months, la_temps, marker='o', linestyle='-', color=single_color, linewidth=2)
ax.plot(months, ny_temps, marker='o', linestyle='-', color=single_color, linewidth=2)
ax.plot(months, chicago_temps, marker='o', linestyle='-', color=single_color, linewidth=2)

ax.set_title("Monthly Temperature Variation Across Cities", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Average Temperature (°C)", fontsize=14)
ax.set_ylim(-5, 30)

# Use the same color for data labels
for i, txt in enumerate(la_temps):
    ax.text(months[i], la_temps[i] + 0.5, str(txt), ha='center', fontsize=10, color=single_color)
for i, txt in enumerate(ny_temps):
    ax.text(months[i], ny_temps[i] + 0.5, str(txt), ha='center', fontsize=10, color=single_color)
for i, txt in enumerate(chicago_temps):
    ax.text(months[i], chicago_temps[i] + 0.5, str(txt), ha='center', fontsize=10, color=single_color)

plt.tight_layout()
plt.show()