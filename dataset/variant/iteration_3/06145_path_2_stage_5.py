import numpy as np
import matplotlib.pyplot as plt

subjects = ['Physics', 'Chemistry', 'Literature', 'Geography', 'Crafts', 'Gym']
study_hours = np.array([5, 6, 4, 3, 2, 1])

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

bar_colors = ['cyan', 'magenta', 'yellow', 'lime', 'coral', 'violet']

bars = ax[1].barh(subjects, study_hours, color=bar_colors, edgecolor='grey', hatch='/')

ax[1].set_title('Hours Dedicated to Learning', fontweight='light', fontsize=14, style='italic')
ax[1].set_xlabel('Time (h)', fontsize=12, fontstyle='oblique')
ax[1].set_ylabel('Disciplines', fontsize=12, fontstyle='oblique')
ax[1].grid(True, linestyle='-.', linewidth=0.8, alpha=0.6)

for bar in bars:
    width = bar.get_width()
    ax[1].annotate(f'{width:.1f}', 
                   xy=(width, bar.get_y() + bar.get_height() / 2), 
                   xytext=(-30, 0), 
                   textcoords='offset points', 
                   ha='right', va='center', fontsize=12, color='gray')

total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

pie_colors = ['#FFB74D', '#7986CB', '#FF7043', '#81C784', '#CE93D8', '#EF5350']

wedges, texts, autotexts = ax[0].pie(study_proportions, labels=subjects, autopct='%1.2f%%', colors=pie_colors, startangle=90, textprops={'fontsize': 10, 'color': 'navy'})

ax[0].set_title('Subjects Study Breakdown', fontweight='heavy', fontsize=13, style='normal')
plt.setp(autotexts, size=10, weight='ultralight')
ax[0].legend(wedges, subjects, title="Fields of Study", loc="upper right")

plt.tight_layout()
plt.show()