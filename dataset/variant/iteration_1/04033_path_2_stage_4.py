import matplotlib.pyplot as plt
import numpy as np

# Original data
activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([55, 90, 45, 70, 65, 80])
well_being_impact = np.array([40, 70, 80, 55, 75, 85])

# Sort indices based on frequencies in ascending order
sorted_indices = frequencies.argsort()
activities_sorted = [activities[i] for i in sorted_indices]
frequencies_sorted = frequencies[sorted_indices]
well_being_impact_sorted = well_being_impact[sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Create bar chart with sorted data
bars = ax1.bar(activities_sorted, frequencies_sorted, color='skyblue', alpha=0.8, label='Frequency of Participation')

# Annotate bars with their height
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height), 
                 xytext=(0, 4),
                 textcoords="offset points",
                 ha='center', va='bottom')

ax1.set_title('Impact of Leisure Activities on Well-being', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Leisure Activities', fontsize=14)
ax1.set_ylabel('Frequency of Participation', fontsize=14, color='skyblue')
ax1.set_ylim(0, 100)
ax1.yaxis.label.set_color('skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.grid(True, linestyle=':', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(activities_sorted, well_being_impact_sorted, color='red', marker='s', linestyle='--', linewidth=2, markersize=8, label='Well-being Impact')
ax2.set_ylabel('Perceived Well-being Impact (0 - 100)', fontsize=14, color='red')
ax2.set_ylim(0, 100)
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', labelcolor='red')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right', fontsize=12)

fig.tight_layout()
plt.show()