import matplotlib.pyplot as plt
import numpy as np

# Using the first row of temperature data for the bar chart
temperature_row = np.array([26, 27, 29, 30, 31, 32, 31, 30, 29, 28])

# Generate labels for the x-axis
labels = [f"Day {i+1}" for i in range(len(temperature_row))]

fig, ax = plt.subplots(figsize=(10, 8))
# Create a horizontal bar chart with new set of colors
ax.barh(labels, temperature_row, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

# Add labels and title
ax.set_xlabel('Temperature')
ax.set_title('Temperature Variation on a Specific Day')
plt.tight_layout()
plt.show()