import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2033)
reading = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])
learning_skills = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
relaxation = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210])

activities = np.array([reading, learning_skills, relaxation])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, activities, colors=['#4682B4', '#FF69B4', '#8A2BE2'], alpha=0.8)

ax.set_title('Projected Personal Time (2023-2032)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Hrs/Yr', fontsize=14)

ax.set_xticks(np.arange(2023, 2033, 1))
ax.set_yticks(np.arange(0, 1001, 100))
ax.set_xlim(2023, 2032)
ax.set_ylim(0, 1000)

ax.plot(years, reading, marker='o', linestyle='-', color='#4682B4')
ax.plot(years, learning_skills, marker='o', linestyle='-', color='#FF69B4')
ax.plot(years, relaxation, marker='o', linestyle='-', color='#8A2BE2')

plt.tight_layout()
plt.show()