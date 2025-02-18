import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2026)

e_learning_platforms = [
    10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 78, 80, 82, 84, 86
]
virtual_classrooms = [
    5, 6, 8, 10, 12, 15, 18, 20, 25, 28, 32, 35, 38, 40, 42, 45, 50, 52, 54, 55, 57
]
educational_apps = [
    2, 3, 5, 7, 9, 11, 15, 18, 22, 27, 30, 35, 40, 43, 47, 50, 53, 55, 58, 60, 63
]

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(years, e_learning_platforms, label='Online Learning Hubs', color='#66b3ff', alpha=0.8)
ax.bar(years, virtual_classrooms, bottom=e_learning_platforms, label='Remote Classrooms', color='#99ff99', alpha=0.8)
combined_base = np.array(e_learning_platforms) + np.array(virtual_classrooms)
ax.bar(years, educational_apps, bottom=combined_base, label='Learning Applications', color='#ff9999', alpha=0.8)

ax.set_title('Shifting Paradigm in Learning (2005-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Adoption Rate (%)', fontsize=14)

ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

ax.grid(alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=12, title='Education Tools')

plt.tight_layout()
plt.show()