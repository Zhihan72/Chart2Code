import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
days = np.arange(1, 31)
exercise_intensity = np.array([
    5, 7, 3, 8, 6, 5, 7, 5, 6, 4, 6, 6, 7, 8, 6, 7, 5, 6, 8, 3, 7, 4, 6, 6,
    5, 6, 5, 7, 8, 7
])
heart_rate_recovery = np.array([
    19, 20, 18, 17, 16, 16, 15, 15, 19, 17, 16, 18, 18, 17, 18, 17, 17, 16,
    20, 17, 16, 18, 18, 16, 17, 19, 16, 15, 16, 17
])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(days, exercise_intensity, color='blue', marker='s', linewidth=1.5, markersize=10)
ax2 = ax.twinx()
ax2.plot(days, heart_rate_recovery, color='green', marker='^', linestyle='-.', linewidth=1.5, markersize=7)

ax.grid(visible=True, linestyle=':', linewidth=1, alpha=0.5)

ax.set_title("Exercise Intensity and Heart Rate Recovery Over Days")
ax.set_xlabel("Days")
ax.set_ylabel("Exercise Intensity")
ax2.set_ylabel("Heart Rate Recovery")

ax.legend(['Exercise Intensity'], loc='upper left')
ax2.legend(['Heart Rate Recovery'], loc='upper right')

plt.tight_layout()
plt.show()