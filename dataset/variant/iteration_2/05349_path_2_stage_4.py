import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2033)
reading = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])
exercise = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240])
learning = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290])
relax = np.array([120, 130, 140, 150, 160, 170, 180, 190, 200, 210])
social = np.array([130, 135, 140, 145, 150, 155, 160, 165, 170, 175])
work = np.array([250, 260, 270, 280, 290, 300, 310, 320, 330, 340])

activities = np.array([reading, exercise, learning, relax, social, work])

fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#4682B4', '#B44682', '#82B446', '#B4B446', '#46B4B4', '#B44B46']

ax.stackplot(years, activities, colors=colors, alpha=0.8)

ax.set_title('Time Spent on Activities: 2023-2032', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Hours/Year', fontsize=14)

ax.set_xticks(np.arange(2023, 2033, 1))
ax.set_yticks(np.arange(0, 1601, 200))
ax.set_xlim(2023, 2032)
ax.set_ylim(0, 1600)

plt.tight_layout()
plt.show()