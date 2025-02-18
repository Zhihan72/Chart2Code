import matplotlib.pyplot as plt
import numpy as np

temperature_row = np.array([26, 27, 29, 30, 31, 32, 31, 30, 29, 28])

labels = [f"Day {i+1}" for i in range(len(temperature_row))]

fig, ax = plt.subplots(figsize=(10, 8))

# Randomly altering stylistic elements for the bar chart
ax.barh(labels, temperature_row, color=['#ff6347', '#6a5acd', '#98fb98', '#ffa07a', '#cd5c5c', '#f0e68c', '#dda0dd', '#5f9ea0', '#ffdab9', '#8b0000'], edgecolor='black', linestyle='--', linewidth=2)

# Alter legend and grid styles
ax.legend(['Temperature'], loc='upper center', frameon=True, shadow=True)
ax.grid(True, linestyle=':', color='gray')

ax.set_xlabel('Temperature', color='seagreen')
ax.set_title('Temperature Variation on a Specific Day', fontsize=14, color='darkred')

plt.tight_layout()
plt.show()