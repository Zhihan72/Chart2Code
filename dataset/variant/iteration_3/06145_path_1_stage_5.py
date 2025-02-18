import numpy as np
import matplotlib.pyplot as plt

subjects = ['Math', 'Sci', 'Eng', 'Hist', 'Art', 'PE']
study_hours = np.array([6, 5, 3, 4, 1, 2])

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

total_study_time = np.sum(study_hours)
study_proportions = study_hours / total_study_time

# Changed colors and added hatch patterns randomly
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
hatches = ['/', '\\', '|', '-', '+', 'x']
wedges, texts, autotexts = ax[0].pie(study_proportions, labels=subjects, autopct='%1.1f%%', 
                                     colors=colors, startangle=90, 
                                     textprops={'fontsize': 10}, 
                                     wedgeprops=dict(width=0.4, hatch=hatches))
ax[0].set_title('Study Time Proportion', fontweight='bold', fontsize=14)
plt.setp(autotexts, size=10, weight='normal')
# Removed legend

# Changed bar color and border
bars = ax[1].bar(subjects, study_hours, color='lightgreen', edgecolor='gray', linestyle='-.')
ax[1].set_title('Weekly Study Hours', fontweight='bold', fontsize=14)
ax[1].set_xlabel('Subject', fontsize=12)
ax[1].set_ylabel('Hours Spent', fontsize=12)
# Changed grid style
ax[1].grid(True, linestyle='-.', linewidth=0.8, alpha=0.5)

for bar in bars:
    height = bar.get_height()
    ax[1].annotate(f'{height:.1f}', 
                   xy=(bar.get_x() + bar.get_width() / 2, height), 
                   xytext=(0, 4), 
                   textcoords='offset points', 
                   ha='center', va='bottom', fontsize=10, color='brown')

plt.tight_layout()
plt.show()