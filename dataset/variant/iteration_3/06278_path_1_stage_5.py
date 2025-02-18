import matplotlib.pyplot as plt

# Sorted data for plotting
sports_sorted = ['Basketball', 'Soccer', 'Baseball', 'Tennis', 'Swimming', 'Volleyball']
wins_sorted = [9, 12, 14, 8, 10, 11]
avg_scores_sorted = [80.5, 3.2, 6.7, 2.4, 85.0, 78.3]

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for number of wins
bars = ax1.bar(sports_sorted, wins_sorted, color='#4682B4', alpha=0.7)

# Line plot for average scores
ax2 = ax1.twinx()
ax2.plot(sports_sorted, avg_scores_sorted, color='#4682B4', marker='o', linestyle='-', linewidth=2)

# Titles and labels
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

# Remove gridlines, legends, and borders
ax1.yaxis.grid(False)
ax1.get_xaxis().set_visible(False)
fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)

# Display the plot
plt.show()