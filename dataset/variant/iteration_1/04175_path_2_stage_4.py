import matplotlib.pyplot as plt
import numpy as np

depts = ['CS', 'ME', 'Psych', 'Bus Admin', 'Arts']
study_hours = [25, 20, 18, 15, 10]
gpas = [3.8, 3.2, 3.6, 3.1, 3.5]

bar_colors = ['#FF7F50', '#6A5ACD', '#FFD700', '#DC143C', '#20B2AA']
line_color = '#8B0000'

fig, ax1 = plt.subplots(figsize=(15, 8))

bars = ax1.bar(depts, study_hours, color=bar_colors, edgecolor='gray', hatch='/', width=0.6)
for bar, hours in zip(bars, study_hours):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, str(hours), ha='center', va='bottom', fontsize=9, fontweight='light', color='blue')

ax2 = ax1.twinx()
ax2.plot(depts, gpas, color=line_color, marker='s', linestyle='--', linewidth=3, markersize=8, label='Avg GPA')

ax1.set_title('Study & Performance by Department', fontsize=18, fontweight='heavy', color='darkgreen')
ax1.set_xlabel('Departments', fontsize=13, labelpad=8, color='navy')
ax1.set_ylabel('Hours Spent Studying', fontsize=13, labelpad=8, color='navy')
ax2.set_ylabel('GPA Score', fontsize=13, labelpad=8, color='navy')

ax1.set_xticks(np.arange(len(depts)))
ax1.set_xticklabels(depts, rotation=30, ha='right', fontsize=9, fontweight='regular', color='darkred')

ax1.set_ylim(0, 30)
ax2.set_ylim(0, 4.0)
ax1.grid(True, which='both', axis='x', linestyle='-.', linewidth=0.9, alpha=0.5)

ax2.legend(loc='lower left', bbox_to_anchor=(0, 1.0))

plt.tight_layout()
plt.show()