import matplotlib.pyplot as plt
import numpy as np

workshop_topics = ['AI', 'Blockchain', 'Cloud']
attendance_data = np.array([
    [10, 15, 20, 25, 30],  # AI
    [8, 12, 15, 20, 25],   # Blockchain
    [7, 11, 16, 21, 27],   # Cloud
])

total_attendance = attendance_data.sum(axis=1)

sorted_indices = np.argsort(-total_attendance)
sorted_topics = [workshop_topics[i] for i in sorted_indices]
sorted_attendance_data = attendance_data[sorted_indices]

# Shuffled colors for the sorted topics
colors = ['#66b3ff', '#ffcc99', '#ff9999']

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sorted_topics))
bar_width = 0.5

ax.bar(bar_positions, total_attendance[sorted_indices], color=colors, edgecolor='white', alpha=0.7, width=bar_width)

ax.set_title("TechVille Workshop Total Attendance (2019-23)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Workshop Topics", fontsize=14)
ax.set_ylabel("Total Attendance (k)", fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_topics)

for i, attendance in enumerate(total_attendance[sorted_indices]):
    ax.text(i, attendance + 1, f'{attendance}k', ha='center', fontsize=10, fontweight='bold')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()