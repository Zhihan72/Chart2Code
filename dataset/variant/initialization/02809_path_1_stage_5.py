import matplotlib.pyplot as plt
import numpy as np

# Data setup
percentage_data = np.array([30, 40, 20, 10, 25, 35, 30, 10])

# Sort data
sorted_indices = np.argsort(percentage_data)  # for ascending sort
# sorted_indices = np.argsort(percentage_data)[::-1]  # for descending sort
sorted_data = percentage_data[sorted_indices]

# Define bar positions
xpos = np.arange(len(sorted_data))

# Plot bars
plt.figure(figsize=(10, 6))
plt.bar(xpos, sorted_data, color='#66B3FF')

# Customize the axes
plt.ylim(0, 50)

# Remove grids and borders
plt.gca().xaxis.set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Display the plot
plt.show()