import matplotlib.pyplot as plt

# Define sports categories and associated data
sports = ['Basketball', 'Soccer', 'Tennis', 'Baseball', 'Swimming']
wins = [9, 12, 8, 14, 10]
avg_scores = [80.5, 3.2, 2.4, 6.7, 85.0]

# Sorted data
sports_sorted = ['Basketball', 'Soccer', 'Baseball', 'Tennis', 'Swimming']
wins_sorted = [9, 12, 14, 8, 10]
avg_scores_sorted = [80.5, 3.2, 6.7, 2.4, 85.0]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for number of wins
bars = ax1.bar(sports_sorted, wins_sorted, color='#4682B4', alpha=0.7)

# Line plot for average scores
ax2 = ax1.twinx()
ax2.plot(sports_sorted, avg_scores_sorted, color='#4682B4', marker='o', linestyle='-', linewidth=2)

# Titles and labels with altered text
ax1.set_title('Team Metrics Overview\nScores and Wins Analysis', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Sports Category', fontsize=12)
ax1.set_ylabel('Wins Count', fontsize=12)
ax2.set_ylabel('Score Average', fontsize=12, color='#4682B4')

# Annotating each bar with the number of wins
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Annotate each point with the average score
for i, value in enumerate(avg_scores_sorted):
    ax2.text(i, value + 0.5, f'{value}', color='#4682B4', fontsize=10, ha='center', va='bottom')

# Gridlines for readability
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Legends
ax1.legend(['Win Count'], loc='upper left', frameon=False)
ax2.legend(['Score Average'], loc='upper right', frameon=False)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()