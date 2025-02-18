import numpy as np
import matplotlib.pyplot as plt

# Title and backstory
# The story revolves around the growth of various fictional non-traditional sports leagues and their cumulative revenue growth
# over a decade. Specifically, it tracks the growth of eSports, Robot Combat, and Drone Racing from 2010 to 2020.

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Fictional revenue data for different sports leagues in billion USD
esports_revenue = np.array([0.5, 0.7, 1.0, 1.4, 1.9, 2.4, 3.0, 3.8, 4.7, 5.8, 7.0])
robot_combat_revenue = np.array([0.3, 0.5, 0.6, 0.8, 1.1, 1.5, 1.9, 2.4, 3.0, 3.7, 4.5])
drone_racing_revenue = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.8, 2.5, 3.3, 4.2, 5.2])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot lines for each sports league
ax.plot(years, esports_revenue, marker='o', linestyle='-', color='red', linewidth=2, label='eSports')
ax.plot(years, robot_combat_revenue, marker='^', linestyle='-', color='blue', linewidth=2, label='Robot Combat')
ax.plot(years, drone_racing_revenue, marker='s', linestyle='-', color='green', linewidth=2, label='Drone Racing')

# Add titles and labels
ax.set_title('Growth of Non-Traditional Sports Leagues\nRevenue from 2010 to 2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (billion USD)', fontsize=12)

# Customize ticks and grid
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend with title
ax.legend(title='Sports League', fontsize=11, loc='upper left')

# Annotations to highlight significant growths
ax.annotate('Exponential Growth',
            xy=(2015, 2.4), xytext=(2013.5, 5),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=11, color='darkred')

ax.annotate('Rising Popularity',
            xy=(2018, 2.4), xytext=(2016, 3), 
            arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=11, color='navy')

# Automatically adjust layout to avoid overlaps
plt.tight_layout()

# Display the plot
plt.show()