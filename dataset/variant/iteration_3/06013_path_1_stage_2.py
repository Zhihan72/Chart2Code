import matplotlib.pyplot as plt
import numpy as np

# Data Construction
missions = ['Apollo 11', 'Apollo 12', 'Apollo 14', 'Apollo 15', 'Apollo 16', 'Apollo 17']
daytime_highs = np.array([130, 127, 125, 128, 123, 127])  # Reordered values
nighttime_lows = np.array([-155, -153, -157, -156, -150, -155])  # Reordered values

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Bar Width
width = 0.4

# Scatter plot of Highs and Lows
x_pos = np.arange(len(missions))  # the label locations

# Plotting the daytime high temperatures and nighttime low temperatures
bars_day = ax.bar(x_pos - width/2, daytime_highs, width, color='orange', edgecolor='black')
bars_night = ax.bar(x_pos + width/2, nighttime_lows, width, color='blue', edgecolor='black')

# Adding grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Automatically adjusting layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()