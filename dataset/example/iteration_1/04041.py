import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the number of steps taken by four friends over a week to explore their daily activity levels.

# Define the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Steps walked each day by each of the four friends (artificial data)
steps_friend_1 = [4000, 4200, 3780, 5000, 5300, 6000, 6200]
steps_friend_2 = [3500, 3650, 3200, 4100, 4300, 4600, 4900]
steps_friend_3 = [4500, 4700, 4900, 5300, 5500, 5800, 6000]
steps_friend_4 = [3000, 3100, 2900, 3500, 3800, 4000, 4100]

# Convert steps data to numpy arrays for easier processing
steps_data = np.array([steps_friend_1, steps_friend_2, steps_friend_3, steps_friend_4])

# Initialize the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data
for i, steps in enumerate(steps_data):
    ax.plot(days, steps, marker='o', linestyle='-', label=f'Friend {i + 1}')

# Title and labels
ax.set_title("Weekly Activity Tracking:\nDaily Steps Taken by Four Friends", fontsize=16, fontweight='bold')
ax.set_xlabel("Day of the Week", fontsize=14)
ax.set_ylabel("Number of Steps", fontsize=14)

# Adding a legend
ax.legend(title="Friends", loc='upper left', fontsize=12, title_fontsize='13')

# Customizing the grid, ticks, and layout for better readability
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xticks(days)
ax.set_yticks(range(0, 7000, 500))
plt.xticks(rotation=45)
plt.tight_layout()

# Adding annotations to highlight key observations
annotations = [
    ("Friends 1 and 3 were most active on Saturday.", 5.5, 6000),
    ("Friend 4's activity level increased gradually.", 6, 4100)
]
for text, x, y in annotations:
    ax.annotate(text, (x, y), xytext=(15, 25), textcoords='offset points',
                arrowprops=dict(arrowstyle="->", color='black'), fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="wheat"))

# Show plot
plt.show()