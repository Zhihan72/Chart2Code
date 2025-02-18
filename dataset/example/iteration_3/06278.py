import matplotlib.pyplot as plt
import numpy as np

# Backstory and title: 
# A local school wants to track the performance of different sports teams over the academic year.
# The chart shows the number of wins and the average scores of each team in various sports.

# Define sports categories
sports = ['Soccer', 'Basketball', 'Baseball', 'Tennis', 'Swimming']

# Number of wins by each sports team
wins = [12, 9, 14, 8, 10]

# Average score for each sports team
avg_scores = [3.2, 80.5, 6.7, 2.4, 85.0]  # Different units due to different sports scoring systems

# Colors for bars
colors = ['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#8A2BE2']

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for number of wins
bars = ax1.bar(sports, wins, color=colors, alpha=0.7)

# Line plot for average scores
ax2 = ax1.twinx()
ax2.plot(sports, avg_scores, color='#FF4500', marker='o', linestyle='-', linewidth=2, label='Average Scores')

# Title and labels
ax1.set_title('School Sports Team Performance\nWins and Average Scores Per Sport', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Sport', fontsize=12)
ax1.set_ylabel('Number of Wins', fontsize=12)
ax2.set_ylabel('Average Scores', fontsize=12, color='#FF4500')

# Annotating each bar with the number of wins
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Annotating each point with the average score
for i, value in enumerate(avg_scores):
    ax2.text(i, value + 0.5, f'{value}', color='#FF4500', fontsize=10, ha='center', va='bottom')

# Gridlines for readability
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Legends
ax1.legend(['Number of Wins'], loc='upper left', frameon=False)
ax2.legend(loc='upper right', frameon=False)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()