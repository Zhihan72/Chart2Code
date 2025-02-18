import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)

exercise_intensity = np.array([
    3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 6, 7, 6, 5, 6, 7, 
    8, 7, 6, 5, 4, 3
])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(days, exercise_intensity, color='blue', marker='o', linewidth=2, markersize=8, label='Intensity Tracker')

# Randomized Titles and Labels
ax.set_title('Monthly Training Evaluation: Intensity Levels', fontsize=18, fontweight='bold')
ax.set_xlabel('Day Counter', fontsize=14)
ax.set_ylabel('Intensity Level (units)', fontsize=14, color='blue')

ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

ax.legend(loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()