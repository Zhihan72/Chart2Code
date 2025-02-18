import matplotlib.pyplot as plt
import numpy as np

times = np.array(['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'])

pop_bands = np.array([2, 3, 5, 7, 9, 10, 8, 6])
rock_bands = np.array([1, 2, 4, 3, 6, 8, 7, 5])
indie_bands = np.array([0, 1, 2, 4, 3, 5, 6, 4])

audience_attendance = np.array([5, 8, 15, 25, 35, 45, 40, 30])

fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharex=True)

common_color = 'purple'

axes[0].plot(times, pop_bands, '-o', color=common_color)
axes[0].plot(times, rock_bands, '-s', color=common_color)
axes[0].plot(times, indie_bands, '-^', color=common_color)
axes[0].grid(alpha=0.3, linestyle='--', linewidth=0.7)

axes[1].plot(times, audience_attendance, '-D', color=common_color)
axes[1].grid(alpha=0.3, linestyle='--', linewidth=0.7)

for ax in axes:
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()