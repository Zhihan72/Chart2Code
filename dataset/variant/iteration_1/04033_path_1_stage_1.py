import matplotlib.pyplot as plt
import numpy as np

activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([80, 65, 90, 55, 45, 70])
well_being_impact = np.array([85, 75, 40, 70, 80, 55])

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.barh(activities, frequencies, color='skyblue', alpha=0.7, label='Frequency of Participation')

for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # 3 points horizontal offset
                textcoords="offset points",
                ha='left', va='center')

ax1.set_title('Impact of Leisure Activities on Well-being', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Frequency of Participation', fontsize=14, color='skyblue')
ax1.set_ylabel('Leisure Activities', fontsize=14)
ax1.set_xlim(0, 100)
ax1.xaxis.label.set_color('skyblue')
ax1.tick_params(axis='x', labelcolor='skyblue')
ax1.grid(True, linestyle='--', alpha=0.6)

ax2 = ax1.twiny()
ax2.plot(well_being_impact, activities, color='coral', marker='o', linestyle='-', linewidth=2, markersize=10, label='Well-being Impact')
ax2.set_xlabel('Perceived Well-being Impact (0 - 100)', fontsize=14, color='coral')
ax2.set_xlim(0, 100)
ax2.xaxis.label.set_color('coral')
ax2.tick_params(axis='x', labelcolor='coral')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower right', fontsize=10)

fig.tight_layout()
plt.show()