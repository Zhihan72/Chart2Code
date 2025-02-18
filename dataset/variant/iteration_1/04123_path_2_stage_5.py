import matplotlib.pyplot as plt
import numpy as np

times = np.array(['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'])

pop_bands = np.array([2, 3, 5, 7, 9, 10, 8, 6])
rock_bands = np.array([1, 2, 4, 3, 6, 8, 7, 5])
audience_attendance = np.array([5, 8, 15, 25, 35, 45, 40, 30])

fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharex=True)

axes[0].plot(times, pop_bands, '-o', color='blue', label='Pop Bands')
axes[0].plot(times, rock_bands, '-s', color='orange', label='Rock Bands')
axes[0].legend()

axes[1].plot(times, audience_attendance, '-D', color='magenta', label='Audience Attendance')
axes[1].legend()

for ax in axes:
    ax.tick_params(axis='x', rotation=45)
    ax.set_frame_on(False)

plt.tight_layout()
plt.show()