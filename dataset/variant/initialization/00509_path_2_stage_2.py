import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
exam_scores = np.array([55, 60, 65, 68, 72, 78, 80, 84, 88, 93])
reading_hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 2, 1.5])
exercises_hours = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.scatter(study_hours, exam_scores, color='teal', edgecolor='black', s=100, alpha=0.7)
X_Y_Spline = make_interp_spline(study_hours, exam_scores, k=3)
X_ = np.linspace(study_hours.min(), study_hours.max(), 500)
Y_ = X_Y_Spline(X_)
ax1.plot(X_, Y_, color='teal', linewidth=2.5)

ax1.set_xlim(0, 22)
ax1.set_ylim(50, 100)

ax2 = ax1.twinx()
bar_width = 0.35
bar_positions = study_hours - bar_width/2

ax2.bar(bar_positions, reading_hours, bar_width, color='teal', alpha=0.6)
ax2.bar(bar_positions + bar_width, exercises_hours, bar_width, color='teal', alpha=0.6)

ax2.set_ylim(0, 6)

ax1.grid(True, linestyle='--', alpha=0.6)
fig.tight_layout()

plt.show()