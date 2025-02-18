import matplotlib.pyplot as plt
import numpy as np

missions = ['Apollo 11', 'Apollo 12', 'Apollo 14', 'Apollo 15', 'Apollo 16', 'Apollo 17']
daytime_highs = np.array([130, 127, 125, 128, 123, 127])
nighttime_lows = np.array([-155, -153, -157, -156, -150, -155])

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.4
x_pos = np.arange(len(missions))

ax.bar(x_pos - width/2, daytime_highs, width, color='blue')
ax.bar(x_pos + width/2, nighttime_lows, width, color='orange')

plt.tight_layout()
plt.show()