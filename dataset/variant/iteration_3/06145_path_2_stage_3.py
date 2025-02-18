import numpy as np
import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History', 'Art', 'Physical Ed']
study_hours = np.array([5, 6, 4, 3, 2, 1])

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Shuffled colors
bar_colors = ['orange', 'blue', 'red', 'green', 'purple', 'pink']

# Plotting the horizontal bar chart with shuffled colors in the second subplot
bars = ax[1].barh(subjects, study_hours, color=bar_colors, edgecolor='black')

ax[1].set_title('Average Weekly Study Hours per Subject\nat Space Academy', fontweight='bold', fontsize=14)
ax[1].set_xlabel('Study Hours', fontsize=12)
ax[1].set_ylabel('Subjects', fontsize=12)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for bar in bars:
    width = bar.get_width()
    ax[1].annotate(f'{width:.1f}', 
                   xy=(width, bar.get_y() + bar.get_height() / 2), 
                   xytext=(3, 0), 
                   textcoords='offset points', 
                   ha='left', va='center', fontsize=12, color='black')

total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

# Shuffled colors for the pie chart now in the first subplot
pie_colors = ['#F57F17', '#5C6BC0', '#F4511E', '#66BB6A', '#AB47BC', '#EC407A']

wedges, texts, autotexts = ax[0].pie(study_proportions, labels=subjects, autopct='%1.1f%%', colors=pie_colors, startangle=140, textprops={'fontsize': 12})

ax[0].set_title('Proportion of Study Time by Subject', fontweight='bold', fontsize=14)
plt.setp(autotexts, size=12, weight='bold')
ax[0].legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()