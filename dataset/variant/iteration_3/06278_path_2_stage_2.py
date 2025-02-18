import matplotlib.pyplot as plt
import numpy as np

sports = ['Swimming', 'Tennis', 'Soccer', 'Basketball', 'Baseball']
wins = [10, 8, 12, 9, 14]
avg_scores = [85.0, 2.4, 3.2, 80.5, 6.7]
colors = ['#8A2BE2', '#FFD700', '#FF6347', '#4682B4', '#3CB371']

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart with altered borders (edgecolor) and transparency
bars = ax1.bar(sports, wins, color=colors, alpha=0.6, edgecolor='black', linewidth=1.2)

# Line plot with new marker and line style
ax2 = ax1.twinx()
ax2.plot(sports, avg_scores, color='#32CD32', marker='s', linestyle='--', linewidth=2, label='Average Scores')

# Title and labels
ax1.set_title('Athletics Overview: Wins and Average Points', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Sports', fontsize=12)
ax1.set_ylabel('Wins', fontsize=12)
ax2.set_ylabel('Average Points', fontsize=12, color='#32CD32')

# Annotations for wins
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Annotations for scores
for i, value in enumerate(avg_scores):
    ax2.text(i, value, f'{value}', color='#32CD32', fontsize=10, ha='center', va='bottom')

# Altered gridlines
ax1.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

# Altered legends
ax1.legend(['Wins'], loc='lower right', frameon=True, shadow=True, facecolor='lightgrey')
ax2.legend(loc='upper center', frameon=True, shadow=True, facecolor='lightgrey')

plt.tight_layout()
plt.show()