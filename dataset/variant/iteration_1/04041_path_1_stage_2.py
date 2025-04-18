import matplotlib.pyplot as plt
import numpy as np

# Define the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Altered steps walked each day by each of the four friends (artificially changed data)
steps_friend_1 = [4100, 4350, 3600, 4900, 5400, 5900, 6050]
steps_friend_2 = [3450, 3750, 3150, 4200, 4550, 4500, 4850]
steps_friend_3 = [4400, 4750, 4950, 5250, 5600, 5750, 6100]
steps_friend_4 = [3050, 3200, 2800, 3550, 3700, 3950, 4050]

# Convert steps data to numpy arrays for easier processing
steps_data = np.array([steps_friend_1, steps_friend_2, steps_friend_3, steps_friend_4])

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
for i, steps in enumerate(steps_data):
    ax.plot(days, steps, marker='o', linestyle='-')

# Customize the grid, ticks, and layout for better readability
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xticks(days)
ax.set_yticks(range(0, 7000, 500))
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()