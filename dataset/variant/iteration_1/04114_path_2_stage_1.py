import matplotlib.pyplot as plt
import numpy as np

# Months and average rainfall (mm)
months = np.arange(1, 13)
rainfall = np.array([85, 78, 92, 110, 134, 158, 102, 75, 65, 45, 40, 70])

# Seasons
season_colors = ['skyblue', 'lightgreen', 'gold', 'coral']
season_labels = [("Winter", 0, 1), ("Spring", 2, 4), ("Summer", 5, 7), ("Autumn", 8, 10)]

fig, ax = plt.subplots(figsize=(14, 8))

# Bar chart
colors = [season_colors[(month - 1) // 3] for month in months]
bars = ax.bar(months, rainfall, color=colors, edgecolor='black')

# Annotate each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                xytext=(0, 3), textcoords='offset points', ha='center', fontsize=10, color='black')

# Titles and labels
ax.set_title("Monthly Rainfall", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Rainfall (mm)", fontsize=14)

# Customize x-ticks
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(months)
ax.set_xticklabels(month_labels, fontsize=12)

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Legend for seasons
handles = [plt.Rectangle((0, 0), 1, 1, color=season_colors[i], edgecolor='black') for i in range(4)]
ax.legend(handles, ['Win', 'Spr', 'Sum', 'Aut'], title="Season", title_fontsize=12, fontsize=10, loc='upper right')

# Annotations
ax.annotate('Rainiest', xy=(5, rainfall[4]), xytext=(6, 150),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='darkblue')
ax.annotate('Dry', xy=(9.5, rainfall[10]), xytext=(8, 90),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, color='darkred')

# Highlight months by seasons
for season, start, end in season_labels:
    ax.axvspan(months[start] - 0.5, months[end + 1] - 0.5, color=season_colors[(start // 3)], alpha=0.1)

plt.tight_layout()
plt.show()