import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
disciplines = ['CS', 'Biz', 'Sci', 'Art', 'Hum']

cs_enrollments = [50, 70, 90, 130, 160, 200, 250, 310, 380, 460, 550]
business_enrollments = [40, 55, 75, 95, 120, 150, 190, 230, 280, 340, 400]
science_enrollments = [30, 40, 55, 70, 85, 105, 130, 160, 200, 240, 290]
arts_enrollments = [20, 25, 35, 50, 60, 80, 95, 115, 140, 170, 200]
humanities_enrollments = [10, 15, 20, 27, 33, 40, 50, 60, 75, 90, 110]

enrollment_data = np.vstack([cs_enrollments, business_enrollments, science_enrollments, arts_enrollments, humanities_enrollments])
total_enrollments = np.sum(enrollment_data, axis=0)

fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, enrollment_data, labels=disciplines, colors=['#32CD32', '#FFD700', '#FF4500', '#800080', '#00BFFF'], alpha=0.5)

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