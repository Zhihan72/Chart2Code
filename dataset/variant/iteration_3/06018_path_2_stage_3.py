import matplotlib.pyplot as plt
import numpy as np

# Define workshop topics and corresponding attendance data
workshop_topics = ['AI', 'Blockchain', 'Cloud']
attendance_data = np.array([
    [10, 15, 20, 25, 30],  # AI
    [8, 12, 15, 20, 25],   # Blockchain
    [7, 11, 16, 21, 27],   # Cloud
])

# Total attendance over the years for each topic
total_attendance = attendance_data.sum(axis=1)

# Sort topics by total attendance in descending order
sorted_indices = np.argsort(-total_attendance)
sorted_topics = [workshop_topics[i] for i in sorted_indices]
sorted_attendance_data = attendance_data[sorted_indices]

# Color map for the sorted topics
colors = ['#ff9999', '#66b3ff', '#ffcc99']

# Create the figure and plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sorted_topics))
bar_width = 0.5

# Create a sorted bar chart for total attendance
ax.bar(bar_positions, total_attendance[sorted_indices], color=colors, edgecolor='white', alpha=0.7, width=bar_width)

# Add title and labels
ax.set_title("TechVille Workshop Total Attendance (2019-23)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Workshop Topics", fontsize=14)
ax.set_ylabel("Total Attendance (k)", fontsize=14)

# Set x-axis labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_topics)

# Annotate bars with exact total attendance
for i, attendance in enumerate(total_attendance[sorted_indices]):
    ax.text(i, attendance + 1, f'{attendance}k', ha='center', fontsize=10, fontweight='bold')

# Add grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()