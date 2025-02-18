import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory:
# In a futuristic city, three high-tech sports—Drone Racing, Robot Wrestling, and AI Chess—are immensely popular among youngsters. 
# This script visualizes the ticket sales for these events across the four seasons of the year 2125.

# Data: Ticket Sales in Thousands
seasons = ["Spring", "Summer", "Autumn", "Winter"]
drone_racing = [50, 80, 60, 70]  # in thousands
robot_wrestling = [40, 60, 50, 65]  # in thousands
ai_chess = [30, 45, 35, 50]  # in thousands

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting Bar Chart
bar_width = 0.25
x = np.arange(len(seasons))  # label locations
br1 = x  # positions for drone racing
br2 = [i + bar_width for i in br1]  # positions for robot wrestling
br3 = [i + bar_width for i in br2]  # positions for AI chess

# Create bars with different colors for each sport
ax.bar(br1, drone_racing, color='orange', width=bar_width, edgecolor='grey', label='Drone Racing')
ax.bar(br2, robot_wrestling, color='blue', width=bar_width, edgecolor='grey', label='Robot Wrestling')
ax.bar(br3, ai_chess, color='green', width=bar_width, edgecolor='grey', label='AI Chess')

# Adding title and labels
ax.set_title('Futuristic Sports Ticket Sales in NeoCity (Year 2125)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Seasons', fontsize=12)
ax.set_ylabel('Tickets Sold (Thousands)', fontsize=12)
ax.set_xticks([r + bar_width for r in range(len(seasons))])
ax.set_xticklabels(seasons)

# Annotate each bar with ticket numbers
for bar, ticket_sales in zip(ax.patches, drone_racing + robot_wrestling + ai_chess):
    height = bar.get_height()
    ax.annotate(f'{ticket_sales}k', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, color='black')

# Adding legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=11, title='Sports Events')

# Add gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap and occlusion
plt.tight_layout()

# Show plot
plt.show()