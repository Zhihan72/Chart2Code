import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A local government conducted a survey to understand the impact of different leisure activities
# on the well-being of their citizens. The survey assessed the frequencies of these activities
# and their perceived impact on mental health.

# Define the leisure activities and their frequencies
activities = ["Exercise", "Reading", "Watching TV", "Socializing", "Traveling", "Cooking"]
frequencies = np.array([80, 65, 90, 55, 45, 70])  # Number of participants engaging in these activities

# Perceived impact on mental well-being (scale: 0 - 100)
well_being_impact = np.array([85, 75, 40, 70, 80, 55])  # Average scores given by participants

# Create the figure and a main axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for activity frequencies
bars = ax1.bar(activities, frequencies, color='skyblue', alpha=0.7, label='Frequency of Participation')

# Adding labels for the bars to show the exact frequency numbers
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Setting the title and labels for the primary y-axis
ax1.set_title('Impact of Leisure Activities on Well-being', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Leisure Activities', fontsize=14)
ax1.set_ylabel('Frequency of Participation', fontsize=14, color='skyblue')
ax1.set_ylim(0, 100)
ax1.yaxis.label.set_color('skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')
ax1.grid(True, linestyle='--', alpha=0.6)

# Create a twin y-axis to show well-being impact scores
ax2 = ax1.twinx()
ax2.plot(activities, well_being_impact, color='coral', marker='o', linestyle='-', linewidth=2, markersize=10, label='Well-being Impact')
ax2.set_ylabel('Perceived Well-being Impact (0 - 100)', fontsize=14, color='coral')
ax2.set_ylim(0, 100)
ax2.yaxis.label.set_color('coral')
ax2.tick_params(axis='y', labelcolor='coral')

# Add legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Adjust layout
fig.tight_layout()
plt.show()