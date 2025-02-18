import matplotlib.pyplot as plt
import numpy as np

# Define years and workshop topics
years = ['2019', '2020', '2021', '2022', '2023']
workshop_topics = ['AI', 'Blockchain', 'Cybersec', 'Cloud']

# Attendance data (in thousands)
attendance_data = np.array([
    [10, 15, 20, 25, 30],  # AI
    [8, 12, 15, 20, 25],   # Blockchain
    [5, 10, 14, 18, 22],   # Cybersec
    [7, 11, 16, 21, 27],   # Cloud
])

# Colors for different workshops
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Create bar charts
bar_width = 0.2
bar_positions = np.arange(len(years))
for i, topic in enumerate(workshop_topics):
    ax.bar(bar_positions + i*bar_width, attendance_data[i], width=bar_width, label=topic, color=colors[i], edgecolor='white', alpha=0.7)

# Add title and labels
ax.set_title("TechVille Workshop Attendance (2019-23)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Attendance (k)", fontsize=14)

# Set x-axis ticks and add grid
ax.set_xticks(bar_positions + bar_width * 1.5)
ax.set_xticklabels(years)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(title="Topics", loc='upper left', bbox_to_anchor=(1.05, 1), frameon=False)

# Annotate bars with exact attendance
for i, topic in enumerate(workshop_topics):
    for j, year in enumerate(years):
        ax.text(bar_positions[j] + i*bar_width, attendance_data[i][j] + 0.5, f'{attendance_data[i][j]}k', ha='center', fontsize=10, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()