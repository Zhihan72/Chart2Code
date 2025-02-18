import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Temperature data for three cities
new_york_temp = [55, 60, 58, 62, 65, 63, 61]
san_francisco_temp = [50, 52, 54, 53, 55, 56, 57]
miami_temp = [75, 77, 76, 78, 80, 81, 82]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the temperature data
ax.plot(days, new_york_temp, marker='o', linestyle='-', color='b')
ax.plot(days, san_francisco_temp, marker='s', linestyle='--', color='g')
ax.plot(days, miami_temp, marker='^', linestyle=':', color='r')

# Add a grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Remove tight_layout since there's no text to prevent overlap
# plt.tight_layout()  # Not necessary anymore

# Display the plot
plt.show()