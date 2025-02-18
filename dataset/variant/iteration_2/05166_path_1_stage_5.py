import matplotlib.pyplot as plt
import numpy as np

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activity_data = np.array([
    [70, 60, 80, 40, 50, 55, 45],
    [60, 30, 65, 50, 45, 35, 40],
    [35, 25, 40, 50, 30, 45, 35],
    [15, 25, 20, 30, 35, 25, 20]
])

stacking_order = [activity_data[0], -activity_data[1], activity_data[2], -activity_data[3]]

fig, ax = plt.subplots(figsize=(14, 8))

for i, data in enumerate(stacking_order):
    ax.bar(days_of_week, data, bottom=np.sum(stacking_order[:i], axis=0) if i % 2 == 0 else -np.sum(np.abs(stacking_order[:i]), axis=0), color='blue')

plt.tight_layout()
plt.savefig("diverging_weekly_activity_levels_no_styles.png")
plt.show()