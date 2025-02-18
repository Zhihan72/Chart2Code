import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)

exercise_intensity = np.array([
    3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 6, 7, 6, 5, 6, 7, 
    8, 7, 6, 5, 4, 3
])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(days, exercise_intensity, marker='o', linewidth=2, markersize=8)

ax.set_title('Monthly Training Evaluation: Intensity Levels')
ax.set_xlabel('Day Counter')
ax.set_ylabel('Intensity Level (units)')

plt.tight_layout()
plt.show()