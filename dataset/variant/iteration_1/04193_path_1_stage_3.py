import matplotlib.pyplot as plt
import numpy as np

# Data (in kilograms)
apples_consumption = [150, 220, 180, 130]
bananas_consumption = [100, 200, 150, 80]
oranges_consumption = [120, 180, 140, 110]

# Aggregate data
data = [apples_consumption, bananas_consumption, oranges_consumption]

# Number of seasons
n_seasons = 4

# Define the positions of the bars
y = np.arange(n_seasons)
bar_height = 0.25

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each fruit's consumption with the same color
single_color = '#3498db'  # A consistent blue color for all bars
for i in range(3):
    bars = ax.barh(y + i * bar_height, data[i], height=bar_height, color=single_color)

# Add gridlines for better readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()