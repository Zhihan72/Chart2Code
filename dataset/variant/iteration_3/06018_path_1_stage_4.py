import matplotlib.pyplot as plt
import numpy as np

years = ['Y2019', 'Y2020', 'Y2021', 'Y2022', 'Y2023']
workshop_topics = ['AI & ML', 'Network Security', 'Cloud Tech']

attendance_data = np.array([
    [10, 15, 20, 25, 30],  
    [5, 10, 14, 18, 22],   
    [7, 11, 16, 21, 27],   
])

colors = ['#ff9999', '#99ff99', '#ffcc99']

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.2
bar_positions = np.arange(len(workshop_topics))
for i, year in enumerate(years):
    ax.barh(bar_positions + i*bar_height, attendance_data[:, i], height=bar_height, color=colors, edgecolor='white', alpha=0.7)

ax.set_title("TechTown's Tech Attendance Festival (2019-2023)", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Topics Discussed", fontsize=14)
ax.set_xlabel("Attendees in Thousands", fontsize=14)

ax.set_yticks(bar_positions + bar_height * 1.5)
ax.set_yticklabels(workshop_topics)

for i in range(len(years)):
    for j in range(len(workshop_topics)):
        ax.text(attendance_data[j][i] + 0.5, bar_positions[j] + i*bar_height, f'{attendance_data[j][i]}k', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()