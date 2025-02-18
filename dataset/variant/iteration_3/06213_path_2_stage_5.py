import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature = [5, 7, 12, 18, 22, 25, 27, 26, 22, 16, 10, 6]
rainfall = [78, 60, 55, 44, 58, 65, 78, 70, 75, 80, 90, 85]  # Added data series for rainfall

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(months, temperature, color='purple', marker='o', linestyle='-', linewidth=2, markersize=5, label='Temperature')
ax.plot(months, rainfall, color='blue', marker='s', linestyle='-', linewidth=2, markersize=5, label='Rainfall')  # New plot for rainfall

ax.set_ylabel('Value')  # Add a label for y-axis
ax.set_title('Monthly Weather Data')
ax.legend()

plt.tight_layout()
plt.show()