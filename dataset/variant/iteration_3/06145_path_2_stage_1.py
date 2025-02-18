import numpy as np
import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History', 'Art', 'Physical Ed']
study_hours = np.array([5, 6, 4, 3, 2, 1])

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Shuffled colors
bar_colors = ['orange', 'blue', 'red', 'green', 'purple', 'pink']

# Plotting the bar chart with shuffled colors
bars = ax[0].bar(subjects, study_hours, color=bar_colors, edgecolor='black')

ax[0].set_title('Average Weekly Study Hours per Subject\nat Space Academy', fontweight='bold', fontsize=14)
ax[0].set_xlabel('Subjects', fontsize=12)
ax[0].set_ylabel('Study Hours', fontsize=12)
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for bar in bars:
    height = bar.get_height()
    ax[0].annotate(f'{height:.1f}', 
                   xy=(bar.get_x() + bar.get_width() / 2, height), 
                   xytext=(0, 3), 
                   textcoords='offset points', 
                   ha='center', va='bottom', fontsize=12, color='black')

total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

# Shuffled colors for the pie chart
pie_colors = ['#F57F17', '#5C6BC0', '#F4511E', '#66BB6A', '#AB47BC', '#EC407A']

wedges, texts, autotexts = ax[1].pie(study_proportions, labels=subjects, autopct='%1.1f%%', colors=pie_colors, startangle=140, textprops={'fontsize': 12})

ax[1].set_title('Proportion of Study Time by Subject', fontweight='bold', fontsize=14)
plt.setp(autotexts, size=12, weight='bold')
ax[1].legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()