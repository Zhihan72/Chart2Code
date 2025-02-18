import matplotlib.pyplot as plt
import numpy as np

missions = ['Apollo 11', 'Apollo 12', 'Apollo 14', 'Apollo 15', 'Apollo 16', 'Apollo 17']
daytime_highs = np.array([130, 127, 125, 128, 123, 127])
nighttime_lows = np.array([-155, -153, -157, -156, -150, -155])

# Sort indices based on daytime_highs in descending order
sorted_indices = np.argsort(daytime_highs)[::-1]

# Sort missions, daytime_highs, and nighttime_lows using the sorted indices
missions_sorted = np.array(missions)[sorted_indices]
daytime_highs_sorted = daytime_highs[sorted_indices]
nighttime_lows_sorted = nighttime_lows[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.4
x_pos = np.arange(len(missions_sorted))

ax.bar(x_pos - width/2, daytime_highs_sorted, width, color='blue', label='Daytime Highs')
ax.bar(x_pos + width/2, nighttime_lows_sorted, width, color='orange', label='Nighttime Lows')

ax.set_xticks(x_pos)
ax.set_xticklabels(missions_sorted)
ax.legend()

plt.tight_layout()
plt.show()