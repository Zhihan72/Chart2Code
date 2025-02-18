import matplotlib.pyplot as plt
import numpy as np

activities = ['Sport', 'Social', 'Entertain', 'Other', 'Study', 'Sleep']
weekday_hours = [2, 2, 3, 3, 6, 8]
weekend_hours = [3, 4, 4, 2, 2, 9]
hybrid_hours = [3, 3, 3.5, 2.5, 4, 8.5]

x_positions = np.arange(len(activities))
bar_width = 0.25

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(x_positions - bar_width, weekday_hours, width=bar_width, color='darkgreen', edgecolor='black')
ax.bar(x_positions, weekend_hours, width=bar_width, color='darkorange', edgecolor='black')
ax.bar(x_positions + bar_width, hybrid_hours, width=bar_width, color='royalblue', edgecolor='black')

ax.set_xticks(x_positions)
ax.set_xticklabels(activities, fontsize=12)

plt.tight_layout()
plt.show()