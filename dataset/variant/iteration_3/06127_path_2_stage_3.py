import matplotlib.pyplot as plt
import numpy as np

hours_range = ['0-3', '4-5', '6-7', '8-9', '10-11', '12+']
weekday_sleepers = [5, 15, 40, 80, 30, 10]
weekend_sleepers = [2, 8, 50, 90, 35, 20]

y_pos = np.arange(len(hours_range))

fig, ax = plt.subplots(figsize=(10, 6))

bar_height = 0.4

new_color_weekday = '#4CAF50'
new_color_weekend = '#F44336'

bars1 = ax.barh(y_pos - bar_height/2, weekday_sleepers, bar_height, color=new_color_weekday, edgecolor='black', alpha=0.7)
bars2 = ax.barh(y_pos + bar_height/2, weekend_sleepers, bar_height, color=new_color_weekend, edgecolor='black', alpha=0.7)

ax.set_yticks(y_pos)
ax.set_yticklabels([''] * len(hours_range))

ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()