import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
disciplines = ['Computer Science', 'Business', 'Science', 'Arts', 'Humanities']

cs_enrollments = [50, 68, 85, 135, 150, 195, 260, 315, 375, 455, 560]
business_enrollments = [35, 60, 78, 98, 115, 145, 185, 235, 270, 330, 390]
science_enrollments = [33, 37, 57, 68, 87, 103, 135, 155, 205, 235, 295]
arts_enrollments = [23, 30, 38, 55, 57, 85, 90, 120, 130, 175, 195]
humanities_enrollments = [12, 17, 23, 29, 31, 42, 55, 58, 78, 92, 115]
enrollment_data = np.vstack([cs_enrollments, business_enrollments, science_enrollments, arts_enrollments, humanities_enrollments])
total_enrollments = np.sum(enrollment_data, axis=0)

fig, ax = plt.subplots(figsize=(14, 9))

ax.stackplot(years, enrollment_data, labels=disciplines, colors=['#B22222', '#228B22', '#9370DB', '#FFD700', '#FF6347'], alpha=0.6)

ax.plot(years, total_enrollments, label='Total Enrollments', color='purple', linewidth=3, marker='s', linestyle='--')

ax.set_title('Tracking Increases in Online Education Enrollment (2015-2025)', fontsize=17, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Enrollments (in thousands)', fontsize=13)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(loc='lower right', title='Disciplines', fontsize=11)
ax.grid(True, linestyle='-.', alpha=0.8)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 901, 50))

plt.tight_layout()
plt.show()