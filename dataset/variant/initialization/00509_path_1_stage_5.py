import matplotlib.pyplot as plt
import numpy as np

study_hours = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
reading_hours = np.array([1, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 2, 1.5])

fig, ax1 = plt.subplots(figsize=(12, 7))

bar_height = 0.35
bar_positions = study_hours - bar_height / 2
ax1.barh(bar_positions, reading_hours, bar_height, color='lightcoral', alpha=0.6)

ax1.set_xlim(0, 6)
ax1.set_ylim(0, 22)

plt.show()