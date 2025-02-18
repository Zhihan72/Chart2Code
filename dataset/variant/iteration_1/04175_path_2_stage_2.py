import matplotlib.pyplot as plt
import numpy as np

depts = ['CS', 'ME', 'BioChem', 'Psych', 'Bus Admin', 'Arts']
study_hours = [25, 20, 22, 18, 15, 10]
gpas = [3.8, 3.2, 3.4, 3.6, 3.1, 3.5]

# New colors for the bars and line
bar_colors = ['#FF7F50', '#6A5ACD', '#3CB371', '#FFD700', '#DC143C', '#20B2AA']
line_color = '#8B0000'

fig, ax1 = plt.subplots(figsize=(15, 8))

bars = ax1.bar(depts, study_hours, color=bar_colors, edgecolor='black', width=0.6)
for bar, hours in zip(bars, study_hours):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, str(hours), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax2 = ax1.twinx()
ax2.plot(depts, gpas, color=line_color, marker='o', linestyle='-', linewidth=2, markersize=7, label='Avg GPA')

ax1.set_title('Study Hours vs GPA by Department', fontsize=16, fontweight='bold')
ax1.set_xlabel('Depts', fontsize=12, labelpad=10)
ax1.set_ylabel('Study Hours', fontsize=12, labelpad=10)
ax2.set_ylabel('GPA', fontsize=12, labelpad=10)

ax1.set_xticks(np.arange(len(depts)))
ax1.set_xticklabels(depts, rotation=45, ha='right', fontsize=10, fontweight='bold')

ax1.set_ylim(0, 30)
ax2.set_ylim(0, 4.0)
ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.9))

plt.tight_layout()
plt.show()