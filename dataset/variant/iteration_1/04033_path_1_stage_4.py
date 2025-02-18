import matplotlib.pyplot as plt
import numpy as np

activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([55, 70, 45, 90, 65, 80])  # Manually shuffled
well_being_impact = np.array([70, 55, 80, 40, 75, 85])  # Manually shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

bars = ax1.barh(activities, frequencies, color='cornflowerblue', alpha=0.7)

for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                ha='left', va='center')

ax1.set_title('Impact of Leisure Activities on Well-being', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Frequency of Participation', fontsize=14, color='cornflowerblue')
ax1.set_ylabel('Leisure Activities', fontsize=14)
ax1.set_xlim(0, 100)
ax1.xaxis.label.set_color('cornflowerblue')
ax1.tick_params(axis='x', labelcolor='cornflowerblue')

ax2 = ax1.twiny()
ax2.plot(well_being_impact, activities, color='cornflowerblue', marker='o', linestyle='-', linewidth=2, markersize=10)
ax2.set_xlabel('Perceived Well-being Impact (0 - 100)', fontsize=14, color='cornflowerblue')
ax2.set_xlim(0, 100)
ax2.xaxis.label.set_color('cornflowerblue')
ax2.tick_params(axis='x', labelcolor='cornflowerblue')

fig.tight_layout()
plt.show()