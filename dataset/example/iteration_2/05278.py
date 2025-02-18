import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the fictional realm of Pylandia, the "Journey of Heroes" is an annual event where heroes from different regions 
# compete in a series of quests to earn points. The event spans over the course of 12 months, and each region has 
# a different point accumulation trend based on quests.

# Data construction
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Point accumulation trends for four different hero regions
regions = ['Norland', 'Sunford', 'Eastoria', 'Westreach']
points_norland = np.array([5, 12, 20, 35, 45, 60, 72, 85, 90, 95, 100, 110])
points_sunford = np.array([4, 10, 25, 30, 35, 50, 65, 75, 95, 110, 125, 130])
points_eastoria = np.array([3, 8, 18, 22, 30, 38, 50, 60, 70, 80, 90, 100])
points_westreach = np.array([2, 15, 22, 28, 36, 48, 56, 62, 70, 80, 85, 90])

# Create subplots to include another element of the event, like the cumulative total points of all regions combined
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Plot cumulative points for all regions for overall event analysis
cumulative_points = points_norland + points_sunford + points_eastoria + points_westreach
ax2.plot(months, cumulative_points, color='purple', linestyle='--', marker='x', label='Total Points', linewidth=2)

# Plot individual regions' points with distinct styles
ax1.plot(months, points_norland, marker='o', linestyle='-', color='blue', linewidth=2, label='Norland')
ax1.plot(months, points_sunford, marker='s', linestyle='-', color='green', linewidth=2, label='Sunford')
ax1.plot(months, points_eastoria, marker='d', linestyle='-', color='red', linewidth=2, label='Eastoria')
ax1.plot(months, points_westreach, marker='^', linestyle='-', color='orange', linewidth=2, label='Westreach')

# Set chart title and labels
ax1.set_title('Journey of Heroes: Point Accumulation Over the Year', fontsize=16, fontweight='bold')
ax1.set_xlabel('Months', fontsize=14)
ax1.set_ylabel('Points per Region', fontsize=14)
ax2.set_ylabel('Cumulative Points', fontsize=14)

# Add grid for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Add legends
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()