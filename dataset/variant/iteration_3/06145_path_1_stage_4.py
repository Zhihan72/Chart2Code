import numpy as np
import matplotlib.pyplot as plt

subjects = ['Math', 'Sci', 'Eng', 'Hist', 'Art', 'PE']
study_hours = np.array([6, 5, 3, 4, 1, 2])

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

colors = plt.cm.Paired(np.linspace(0, 1, len(subjects)))
wedges, texts, autotexts = ax[0].pie(study_proportions, labels=subjects, autopct='%1.1f%%', colors=colors, startangle=140, textprops={'fontsize': 12}, wedgeprops=dict(width=0.3))
ax[0].set_title('Study Time %', fontweight='bold', fontsize=12)
plt.setp(autotexts, size=12, weight='bold')
ax[0].legend(wedges, subjects, title="Subjects", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

bars = ax[1].bar(subjects, study_hours, color='skyblue', edgecolor='black')
ax[1].set_title('Weekly Study Hours', fontweight='bold', fontsize=12)
ax[1].set_xlabel('Subj', fontsize=11)
ax[1].set_ylabel('Hours', fontsize=11)
ax[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

for bar in bars:
    height = bar.get_height()
    ax[1].annotate(f'{height:.1f}', 
                   xy=(bar.get_x() + bar.get_width() / 2, height), 
                   xytext=(0, 3), 
                   textcoords='offset points', 
                   ha='center', va='bottom', fontsize=11, color='black')

plt.tight_layout()
plt.show()