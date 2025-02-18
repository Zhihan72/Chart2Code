import matplotlib.pyplot as plt

# Define sports categories and associated data
sports = ['Soccer', 'Basketball', 'Baseball', 'Tennis', 'Swimming']
wins = [12, 9, 14, 8, 10]
avg_scores = [3.2, 80.5, 6.7, 2.4, 85.0]

# Sort data by the number of wins in descending order
sorted_indices = sorted(range(len(wins)), key=lambda i: wins[i], reverse=True)
sports_sorted = [sports[i] for i in sorted_indices]
wins_sorted = [wins[i] for i in sorted_indices]
avg_scores_sorted = [avg_scores[i] for i in sorted_indices]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for number of wins
bars = ax1.bar(sports_sorted, wins_sorted, color='#4682B4', alpha=0.7)

# Line plot for average scores
ax2 = ax1.twinx()
ax2.plot(sports_sorted, avg_scores_sorted, color='#4682B4', marker='o', linestyle='-', linewidth=2)

# Title and labels
ax1.set_title('School Sports Team Performance\nWins and Average Scores Per Sport', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Sport', fontsize=12)
ax1.set_ylabel('Number of Wins', fontsize=12)
ax2.set_ylabel('Average Scores', fontsize=12, color='#4682B4')

# Annotating each bar with the number of wins
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Annotating each point with the average score
for i, value in enumerate(avg_scores_sorted):
    ax2.text(i, value + 0.5, f'{value}', color='#4682B4', fontsize=10, ha='center', va='bottom')

# Gridlines for readability
ax1.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Legends
ax1.legend(['Number of Wins'], loc='upper left', frameon=False)
ax2.legend(['Average Scores'], loc='upper right', frameon=False)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()