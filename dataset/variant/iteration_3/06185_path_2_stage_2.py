import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
exercise_intensity = np.array([
    3, 4, 5, 6, 7, 6, 5, 6, 7, 8, 7, 6, 5, 7, 8, 7, 6, 5, 6, 7, 6, 5, 6, 7, 
    8, 7, 6, 5, 4, 3
])
heart_rate_recovery = np.array([
    20, 18, 19, 17, 16, 17, 18, 17, 16, 15, 16, 17, 18, 16, 15, 16, 17, 18, 
    17, 16, 17, 18, 17, 16, 15, 16, 17, 18, 19, 20
])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(days, exercise_intensity, color='red', marker='o', linewidth=2, markersize=8)
ax2 = ax.twinx()
ax2.plot(days, heart_rate_recovery, color='orange', marker='x', linestyle='--', linewidth=2, markersize=8)

ax.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()