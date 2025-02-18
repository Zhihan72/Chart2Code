import matplotlib.pyplot as plt
import numpy as np

sports = ['Swimming', 'Tennis', 'Basketball', 'Baseball']
wins = [10, 8, 9, 14]
avg_scores = [85.0, 2.4, 80.5, 6.7]
colors = ['#FF6347', '#4682B4', '#9ACD32', '#FF1493']  # New set of colors

fig, ax1 = plt.subplots(figsize=(10, 6))

bars = ax1.bar(sports, wins, color=colors, alpha=0.6, edgecolor='black', linewidth=1.2)

ax2 = ax1.twinx()
ax2.plot(sports, avg_scores, color='#FF4500', marker='s', linestyle='--', linewidth=2, label='Average Scores')  # New line color

ax1.set_title('Athletics Overview: Wins and Average Points', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Sports', fontsize=12)
ax1.set_ylabel('Wins', fontsize=12)
ax2.set_ylabel('Average Points', fontsize=12, color='#FF4500')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom', fontsize=10, fontweight='bold')

for i, value in enumerate(avg_scores):
    ax2.text(i, value, f'{value}', color='#FF4500', fontsize=10, ha='center', va='bottom')

ax1.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.5)

ax1.legend(['Wins'], loc='lower right', frameon=True, shadow=True, facecolor='lightgrey')
ax2.legend(loc='upper center', frameon=True, shadow=True, facecolor='lightgrey')

plt.tight_layout()
plt.show()