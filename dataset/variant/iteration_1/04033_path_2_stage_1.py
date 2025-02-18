import matplotlib.pyplot as plt
import numpy as np

# Define the leisure activities and their frequencies
activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([80, 65, 90, 55, 45, 70])  # Number of participants engaging in these activities

# Perceived impact on mental well-being (scale: 0 - 100)
well_being_impact = np.array([85, 75, 40, 70, 80, 55])

# Create the figure and a main axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for activity frequencies
bars = ax1.bar(activities, frequencies, color='lightgreen', alpha=0.8, label='Frequency of Participation')

for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height), 
                 xytext=(0, 4),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Setting the title and labels for the primary y-axis
ax1.set_title('Impact of Leisure Activities on Well-being', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Leisure Activities', fontsize=14)
ax1.set_ylabel('Frequency of Participation', fontsize=14, color='lightgreen')
ax1.set_ylim(0, 100)
ax1.yaxis.label.set_color('lightgreen')
ax1.tick_params(axis='y', labelcolor='lightgreen')
ax1.grid(True, linestyle=':', alpha=0.5)

# Create a twin y-axis to show well-being impact scores
ax2 = ax1.twinx()
ax2.plot(activities, well_being_impact, color='orange', marker='s', linestyle='--', linewidth=2, markersize=8, label='Well-being Impact')
ax2.set_ylabel('Perceived Well-being Impact (0 - 100)', fontsize=14, color='orange')
ax2.set_ylim(0, 100)
ax2.yaxis.label.set_color('orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Add legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right', fontsize=12)

# Adjust layout
fig.tight_layout()
plt.show()