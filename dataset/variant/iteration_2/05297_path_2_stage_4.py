import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
disciplines = ['CS', 'Biz', 'Sci', 'Art', 'Hum']

# Randomly altered enrollments within same dimensional structure
cs_enrollments = [50, 75, 95, 125, 175, 195, 240, 320, 360, 440, 510]
business_enrollments = [45, 60, 80, 105, 115, 145, 180, 220, 275, 330, 390]
science_enrollments = [35, 45, 60, 75, 95, 110, 135, 165, 190, 235, 295]
arts_enrollments = [25, 30, 40, 55, 65, 85, 90, 120, 145, 165, 205]
humanities_enrollments = [15, 20, 25, 30, 35, 45, 55, 65, 80, 85, 115]

enrollment_data = np.vstack([cs_enrollments, business_enrollments, science_enrollments, arts_enrollments, humanities_enrollments])
total_enrollments = np.sum(enrollment_data, axis=0)

fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, enrollment_data, labels=disciplines, colors=['blue']*5, alpha=0.5)

ax.plot(years, total_enrollments, label='Total Enroll', color='navy', linewidth=3, linestyle='--', marker='s')

ax.set_title('Online Edu Growth (2015-25)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Enrollments (k)', fontsize=12)

ax.legend(loc='upper left', title='Subjects', fontsize=9, frameon=True, shadow=True)

ax.grid(True, linestyle='-', alpha=0.3)
plt.xticks(years, rotation=30)
plt.yticks(np.arange(0, 901, 100))

plt.tight_layout()
plt.show()