import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2026)

# Data for the positive side
e_learning_platforms_positive = [10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 86]
# Data for the negative side
virtual_classrooms_negative = [-5, -6, -8, -10, -12, -15, -18, -20, -25, -28, -32, -35, -38, -40, -42, -45, -50, -52, -54, -55, -57]
# Data for additions on the positive side
educational_apps_positive = [2, 3, 5, 7, 9, 11, 15, 18, 22, 27, 30, 35, 40, 43, 47, 50, 53, 55, 58, 60, 63]

fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(years, e_learning_platforms_positive, label='Online Learning Hubs', color='#99ff99', alpha=0.6, linestyle='-')
ax.barh(years, virtual_classrooms_negative, label='Remote Classrooms', color='#ff9999', alpha=0.7, linestyle=':')
ax.barh(years, educational_apps_positive, left=e_learning_platforms_positive, label='Learning Applications', color='#66b3ff', alpha=0.9, linestyle='--')

ax.set_title('Shifting Paradigm in Learning (2005-2025)', fontsize=17, fontweight='bold', pad=30)
ax.set_xlabel('Adoption Rate (%)', fontsize=13)
ax.set_ylabel('Timeline', fontsize=13)

ax.set_yticks(years[::2])
ax.set_yticklabels(years[::2])

ax.axvline(0, color='grey', linewidth=1.2)
ax.grid(alpha=0.4, linestyle='-.')

ax.legend(loc='upper left', fontsize=10, title='Education Tools', title_fontsize='13')

plt.tight_layout()
plt.show()