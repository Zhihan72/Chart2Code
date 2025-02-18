import matplotlib.pyplot as plt
import numpy as np

pages = np.array([120, 200, 320, 400, 150, 220, 300, 50, 180, 290])
ratings = np.array([7, 8, 9, 6, 7, 8, 9, 5, 7, 9])
reading_duration = np.array([8, 12, 18, 22, 9, 13, 17, 5, 10, 15])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Altered scatter plot styling
scatter = ax1.scatter(pages, ratings, color='teal', label='Satisfaction Rating', alpha=0.6, s=120, marker='D', edgecolor='gray')

# Trendline style changes
coef = np.polyfit(pages, ratings, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(pages, poly1d_fn(pages), color='navy', linestyle='-.', linewidth=2, label='Rating Trendline')

ax1.set_xlabel('Number of Pages in Book', fontsize=12)
ax1.set_ylabel('Satisfaction Rating (1-10)', color='teal', fontsize=12)
ax1.tick_params(axis='y', labelcolor='teal')
ax1.set_xlim(0, 450)
ax1.set_ylim(4, 10)

# Secondary y-axis with altered style
ax2 = ax1.twinx()
ax2.plot(pages, reading_duration, color='purple', marker='^', linestyle=':', linewidth=3, label='Reading Duration')
ax2.set_ylabel('Average Reading Duration (hours)', color='purple', fontsize=12)
ax2.tick_params(axis='y', labelcolor='purple')
ax2.set_ylim(0, 25)

# Updated title and grid style
plt.title('Analyzing Book Length, Satisfaction & Reading Time', fontsize=16, fontweight='bold', pad=15)
ax1.grid(True, linestyle='-.', alpha=0.4)

# Randomized legend position
fig.tight_layout()
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', frameon=True, shadow=True)

plt.show()