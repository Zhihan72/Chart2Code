import numpy as np
import matplotlib.pyplot as plt

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional revenue data for different sports leagues in billion USD
esports_revenue = np.array([0.5, 0.7, 1.0, 1.4, 1.9, 2.4, 3.0, 3.8, 4.7, 5.8, 7.0])
robot_combat_revenue = np.array([0.3, 0.5, 0.6, 0.8, 1.1, 1.5, 1.9, 2.4, 3.0, 3.7, 4.5])
drone_racing_revenue = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.8, 2.5, 3.3, 4.2, 5.2])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot lines for each sports league
ax.plot(years, esports_revenue, marker='o', linestyle='-', color='red', linewidth=2)
ax.plot(years, robot_combat_revenue, marker='^', linestyle='-', color='blue', linewidth=2)
ax.plot(years, drone_racing_revenue, marker='s', linestyle='-', color='green', linewidth=2)

# Add titles and labels
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (billion USD)', fontsize=12)

# Customize ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Automatically adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()