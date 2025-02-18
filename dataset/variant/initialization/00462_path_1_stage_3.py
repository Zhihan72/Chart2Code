import matplotlib.pyplot as plt
import numpy as np

# Using the first row of temperature data for the bar chart
temperature_row = np.array([26, 27, 29, 30, 31, 32, 31, 30, 29, 28])

# Generate labels for the x-axis
labels = [f"Day {i+1}" for i in range(len(temperature_row))]

fig, ax = plt.subplots(figsize=(10, 8))
# Create a horizontal bar chart
ax.barh(labels, temperature_row, color='hotpink')

# Add labels and legend
ax.set_xlabel('Temperature')
ax.set_title('Temperature Variation on a Specific Day')
ax.grid(False)
plt.tight_layout()
plt.show()