import matplotlib.pyplot as plt
import numpy as np

# Define years and workshop topics
years = ['2019', '2020', '2021', '2022', '2023']
workshop_topics = ['AI & ML', 'Blockchain', 'Cybersecurity', 'Cloud Computing']

# Attendance data (in thousands)
attendance_data = np.array([
    [10, 15, 20, 25, 30],  # AI & ML
    [8, 12, 15, 20, 25],   # Blockchain
    [5, 10, 14, 18, 22],   # Cybersecurity
    [7, 11, 16, 21, 27],   # Cloud Computing
])

# Colors for different workshops
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create the figure and subplot
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar charts
bar_height = 0.2
bar_positions = np.arange(len(workshop_topics))
for i, year in enumerate(years):
    ax.barh(bar_positions + i*bar_height, attendance_data[:, i], height=bar_height, color=colors, edgecolor='white', alpha=0.7)

# Add title and labels
ax.set_title("TechVille's Annual Technology Workshop Attendance (2019-2023)", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Workshop Topics", fontsize=14)
ax.set_xlabel("Attendance (in thousands)", fontsize=14)

# Set y-axis ticks and labels
ax.set_yticks(bar_positions + bar_height * 1.5)
ax.set_yticklabels(workshop_topics)

# Annotate bars with exact attendance
for i in range(len(years)):
    for j in range(len(workshop_topics)):
        ax.text(attendance_data[j][i] + 0.5, bar_positions[j] + i*bar_height, f'{attendance_data[j][i]}k', va='center', fontsize=10, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()