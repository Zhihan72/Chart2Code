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

# Altered colors for the sorted topics
colors = ['#ff9999', '#66b3ff', '#ffcc99']

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(sorted_topics))
bar_width = 0.4

# Adjust marker types: using hatch patterns
ax.bar(bar_positions, total_attendance[sorted_indices], color=colors, edgecolor='black', hatch='/', alpha=0.8, width=bar_width)

ax.set_title("TechVille Workshop Total Attendance (2019-23)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Workshop Topics", fontsize=13, fontstyle='italic')
ax.set_ylabel("Total Attendance (k)", fontsize=13, fontstyle='italic')
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_topics, fontsize=12)

# Alter text style
for i, attendance in enumerate(total_attendance[sorted_indices]):
    ax.text(i, attendance + 1, f'{attendance}k', ha='center', fontsize=11, color='blue', fontweight='normal')

# Change grid style
ax.yaxis.grid(True, linestyle='-', alpha=0.4)

plt.tight_layout()
plt.show()